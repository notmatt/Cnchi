#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cnchi.py
#
#  Copyright © 2013-2017 Antergos
#
#  This file is part of Cnchi.
#
#  Cnchi is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  Cnchi is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  The following additional terms are in effect as per Section 7 of the license:
#
#  The preservation of all legal notices and author attributions in
#  the material or in the Appropriate Legal Notices displayed
#  by works containing it is required.
#
#  You should have received a copy of the GNU General Public License
#  along with Cnchi; If not, see <http://www.gnu.org/licenses/>.

""" Main Cnchi (Antergos Installer) module """


import os
import sys
import shutil

CNCHI_PATH = "/usr/share/cnchi"
sys.path.append(CNCHI_PATH)
sys.path.append(os.path.join(CNCHI_PATH, "src"))
sys.path.append(os.path.join(CNCHI_PATH, "src/download"))
sys.path.append(os.path.join(CNCHI_PATH, "src/hardware"))
sys.path.append(os.path.join(CNCHI_PATH, "src/installation"))
sys.path.append(os.path.join(CNCHI_PATH, "src/misc"))
sys.path.append(os.path.join(CNCHI_PATH, "src/pacman"))
sys.path.append(os.path.join(CNCHI_PATH, "src/pages"))
sys.path.append(os.path.join(CNCHI_PATH, "src/parted3"))

import logging
import logging.handlers
import gettext
import locale
import uuid
import gi
import requests
import json

import misc.extra as misc
import info
import updater
from logging_utils import ContextFilter


import gtk.show_message as show


try:
    from bugsnag.handlers import BugsnagHandler
    import bugsnag
    BUGSNAG_ERROR = None
except ImportError as err:
    BUGSNAG_ERROR = str(err)

# Useful vars for gettext (translations)
APP_NAME = "cnchi"
LOCALE_DIR = "/usr/share/locale"

# Command line options
cmd_line = None

# At least this GTK version is needed
GTK_VERSION_NEEDED = "3.18.0"


def setup_logging():
    """ Configure our logger """
    logger = logging.getLogger()

    logger.handlers = []

    if cmd_line.debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logger.setLevel(log_level)

    context_filter = ContextFilter()
    logger.addFilter(context_filter.filter)

    # Log format
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(filename)s(%(lineno)d) %(funcName)s(): %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S")

    # File logger
    try:
        file_handler = logging.FileHandler('/tmp/cnchi.log', mode='w')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except PermissionError as permission_error:
        print("Can't open /tmp/cnchi.log : ", permission_error)

    # Stdout logger
    if cmd_line.verbose:
        # Show log messages to stdout
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    if cmd_line.log_server:
        log_server = cmd_line.log_server

        if log_server == 'bugsnag':
            if not BUGSNAG_ERROR:
                # Bugsnag logger
                bugsnag_api = context_filter.api_key
                if bugsnag_api is not None:
                    bugsnag.configure(
                        api_key=bugsnag_api,
                        app_version=info.CNCHI_VERSION,
                        project_root='/usr/share/cnchi/cnchi',
                        release_stage=info.CNCHI_RELEASE_STAGE)
                    bugsnag_handler = BugsnagHandler(api_key=bugsnag_api)
                    bugsnag_handler.setLevel(logging.WARNING)
                    bugsnag_handler.setFormatter(formatter)
                    bugsnag_handler.addFilter(context_filter.filter)
                    bugsnag.before_notify(
                        context_filter.bugsnag_before_notify_callback)
                    logger.addHandler(bugsnag_handler)
                    logging.info(
                        "Sending Cnchi log messages to bugsnag server (using python-bugsnag).")
                else:
                    logging.warning(
                        "Cannot read the bugsnag api key, logging to bugsnag is not possible.")
            else:
                logging.warning(BUGSNAG_ERROR)
        else:
            # Socket logger
            socket_handler = logging.handlers.SocketHandler(
                log_server,
                logging.handlers.DEFAULT_TCP_LOGGING_PORT)
            socket_formatter = logging.Formatter(formatter)
            socket_handler.setFormatter(socket_formatter)
            logger.addHandler(socket_handler)

            # Also add uuid filter to requests logs
            logger_requests = logging.getLogger(
                "requests.packages.urllib3.connectionpool")
            logger_requests.addFilter(context_filter.filter)

            uid = str(uuid.uuid1()).split("-")
            myuid = uid[3] + "-" + uid[1] + "-" + uid[2] + "-" + uid[4]
            logging.info(
                "Sending Cnchi logs to {0} with id '{1}'".format(log_server, myuid))




def check_pyalpm_version():
    """ Checks python alpm binding and alpm library versions """
    try:
        import pyalpm

        txt = "Using pyalpm v{0} as interface to libalpm v{1}"
        txt = txt.format(pyalpm.version(), pyalpm.alpmversion())
        logging.info(txt)
    except (NameError, ImportError) as err:
        try:
            import show_message as show
            show.error(None, err)
        except ImportError as import_error:
            logging.error(import_error)
        finally:
            logging.error(err)
            return False

    return True


def check_iso_version():
    """ Hostname contains the ISO version """
    from socket import gethostname
    hostname = gethostname()
    # antergos-year.month-iso
    prefix = "ant-"
    suffix = "-min"
    if hostname.startswith(prefix) or hostname.endswith(suffix):
        # We're running form the ISO, register which version.
        if suffix in hostname:
            version = hostname[len(prefix):-len(suffix)]
        else:
            version = hostname[len(prefix):]
        logging.debug("Running from ISO version %s", version)
        # Delete user's chromium cache (just in case)
        cache_dir = "/home/antergos/.cache/chromium"
        if os.path.exists(cache_dir):
            shutil.rmtree(path=cache_dir, ignore_errors=True)
            logging.debug("User's chromium cache deleted")
        # If we're running from sonar iso force a11y parameter to true
        if hostname.endswith("sonar"):
            cmd_line.a11y = True
    else:
        logging.debug("Not running from ISO")
    return True


def parse_options():
    """ argparse http://docs.python.org/3/howto/argparse.html """

    import argparse

    desc = _("Cnchi v{0} - Antergos Installer").format(info.CNCHI_VERSION)
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        "-a", "--a11y",
        help=_("Set accessibility feature on by default"),
        action="store_true")
    parser.add_argument(
        "-c", "--cache",
        help=_("Use pre-downloaded xz packages when possible"),
        nargs='?')
    parser.add_argument(
        "-d", "--debug",
        help=_("Sets Cnchi log level to 'debug'"),
        action="store_true")
    parser.add_argument(
        "-e", "--environment",
        help=_("Sets the Desktop Environment that will be installed"),
        nargs='?')
    parser.add_argument(
        "-f", "--force",
        help=_("Runs cnchi even if it detects that another instance is running"),
        action="store_true")
    parser.add_argument(
        "-i", "--disable-tryit",
        help=_("Disables first screen's 'try it' option"),
        action="store_true")
    parser.add_argument(
        "-n", "--no-check",
        help=_("Makes checks optional in check screen"),
        action="store_true")
    parser.add_argument(
        "-p", "--packagelist",
        help=_(
            "Install the packages referenced by a local xml instead of the default ones"),
        nargs='?')
    parser.add_argument(
        "-s", "--log-server",
        help=_("Choose to which log server send Cnchi logs."
               " Expects a hostname or an IP address"),
        nargs='?')
    parser.add_argument(
        "-u", "--update",
        help=_("Upgrade/downgrade Cnchi to the web version"),
        action="store_true")
    parser.add_argument(
        "--disable-update",
        help=_("Do not search for new Cnchi versions online"),
        action="store_true")
    parser.add_argument(
        "-v", "--verbose",
        help=_("Show logging messages to stdout"),
        action="store_true")
    parser.add_argument(
        "-V", "--version",
        help=_("Show Cnchi version and quit"),
        action="store_true")
    parser.add_argument(
        "-z", "--z_hidden",
        help=_("Show options in development (for developers only, do not use this!)"),
        action="store_true")

    return parser.parse_args()


def setup_gettext():
    """ This allows to translate all py texts (not the glade ones) """

    gettext.textdomain(APP_NAME)
    gettext.bindtextdomain(APP_NAME, LOCALE_DIR)

    locale_code, encoding = locale.getdefaultlocale()
    lang = gettext.translation(APP_NAME, LOCALE_DIR, [locale_code], None, True)
    lang.install()


def check_for_files():
    """ Check for some necessary files. Cnchi can't run without them """
    paths = [
        "/usr/share/cnchi",
        "/usr/share/cnchi/ui",
        "/usr/share/cnchi/data",
        "/usr/share/cnchi/data/locale"]

    for path in paths:
        if not os.path.exists(path):
            print(_("Cnchi files not found. Please, install Cnchi using pacman"))
            return False

    return True


def init_cnchi():
    """ This function initialises Cnchi """

    # Sets SIGTERM handler, so Cnchi can clean up before exiting
    # signal.signal(signal.SIGTERM, sigterm_handler)

    # Configures gettext to be able to translate messages, using _()
    setup_gettext()

    # Command line options
    global cmd_line
    cmd_line = parse_options()

    if cmd_line.version:
        print(_("Cnchi (Antergos Installer) version {0}").format(
            info.CNCHI_VERSION))
        sys.exit(0)

    if cmd_line.force:
        misc.remove_temp_files()

    # Drop root privileges
    misc.drop_privileges()

    # Setup our logging framework
    setup_logging()

    # Check Cnchi is correctly installed
    if not check_for_files():
        sys.exit(1)

    # Check installed GTK version
    if not check_gtk_version():
        sys.exit(1)

    # Check installed pyalpm and libalpm versions
    if not check_pyalpm_version():
        sys.exit(1)

    # Check ISO version where Cnchi is running from
    if not check_iso_version():
        sys.exit(1)

    # if not cmd_line.disable_update:
        # update_cnchi()

    # Init PyObject Threads
    threads_init()


if __name__ == '__main__':
    init_cnchi()

    # Create Gtk Application
    app = CnchiApp()
    exit_status = app.run(None)
    sys.exit(exit_status)
