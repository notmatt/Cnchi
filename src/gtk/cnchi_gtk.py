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

import logging
import logging.handlers
import gettext
import locale
import uuid
import gi
import requests
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk, GObject

import gtk.show_message_gtk

import info
import updater
from logging_utils import ContextFilter

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


class CnchiApp(Gtk.Application):
    """ Main Cnchi App class """

    def __init__(self):
        """ Constructor. Call base class """
        Gtk.Application.__init__(self,
                                 application_id="com.antergos.cnchi",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.TMP_RUNNING = "/tmp/.setup-running"

    def do_activate(self):
        """ Override the 'activate' signal of GLib.Application. """
        try:
            import main_window
        except ImportError as err:
            msg = "Cannot create Cnchi main window: {0}".format(err)
            logging.error(msg)
            sys.exit(1)

        # Check if we have administrative privileges
        if os.getuid() != 0:
            msg = _('This installer must be run with administrative privileges, '
                    'and cannot continue without them.')
            show_message_gtk.error(None, msg)
            return

        # Check if we're already running
        if self.already_running():
            msg = _("You cannot run two instances of this installer.\n\n"
                    "If you are sure that the installer is not already running\n"
                    "you can run this installer using the --force option\n"
                    "or you can manually delete the offending file.\n\n"
                    "Offending file: '{0}'").format(self.TMP_RUNNING)
            show_message_gtk.error(None, msg)
            return

        window = main_window.MainWindow(self, cmd_line)
        self.add_window(window)
        window.show()

        with open(self.TMP_RUNNING, "w") as tmp_file:
            txt = "Cnchi {0}\n{1}\n".format(info.CNCHI_VERSION, os.getpid())
            tmp_file.write(txt)

        # This is unnecessary as show_all is called in MainWindow
        # window.show_all()

        # def do_startup(self):
        # """ Override the 'startup' signal of GLib.Application. """
        # Gtk.Application.do_startup(self)

        # Application main menu (we don't need one atm)
        # Leaving this here for future reference
        # menu = Gio.Menu()
        # menu.append("About", "win.about")
        # menu.append("Quit", "app.quit")
        # self.set_app_menu(menu)

    def already_running(self):
        """ Check if we're already running """
        if os.path.exists(self.TMP_RUNNING):
            logging.debug("File %s already exists.", self.TMP_RUNNING)
            with open(self.TMP_RUNNING) as setup:
                lines = setup.readlines()
            if len(lines) >= 2:
                try:
                    pid = int(lines[1].strip('\n'))
                except ValueError as err:
                    logging.debug(err)
                    logging.debug("Cannot read PID value.")
                    return True
            else:
                logging.debug("Cannot read PID value.")
                return True

            if misc.check_pid(pid):
                logging.info("Cnchi with pid '%d' already running.", pid)
                return True
            else:
                # Cnchi with pid 'pid' is no longer running, we can safely
                # remove the offending file and continue.
                os.remove(self.TMP_RUNNING)
        return False

    def check_gtk_version(self):
        """ Check GTK version """
        # Check desired GTK Version
        major_needed = int(GTK_VERSION_NEEDED.split(".")[0])
        minor_needed = int(GTK_VERSION_NEEDED.split(".")[1])
        micro_needed = int(GTK_VERSION_NEEDED.split(".")[2])

        # Check system GTK Version
        major = Gtk.get_major_version()
        minor = Gtk.get_minor_version()
        micro = Gtk.get_micro_version()

        # Cnchi will be called from our liveCD that already
        # has the latest GTK version. This is here just to
        # help testing Cnchi in our environment.
        wrong_gtk_version = False
        if major_needed > major:
            wrong_gtk_version = True
        if major_needed == major and minor_needed > minor:
            wrong_gtk_version = True
        if major_needed == major and minor_needed == minor and micro_needed > micro:
            wrong_gtk_version = True

        if wrong_gtk_version:
            text = "Detected GTK version {0}.{1}.{2} but version >= {3} is needed."
            text = text.format(major, minor, micro, GTK_VERSION_NEEDED)
            try:
                show_message_gtk.error(None, text)
            except ImportError as import_error:
                logging.error(import_error)
            finally:
                return False
        else:
            logging.info("Using GTK v{0}.{1}.{2}".format(major, minor, micro))

        return True

def threads_init():
    """
    For applications that wish to use Python threads to interact with the GNOME platform,
    GObject.threads_init() must be called prior to running or creating threads and starting
    main loops (see notes below for PyGObject 3.10 and greater). Generally, this should be done
    in the first stages of an applications main entry point or right after importing GObject.
    For multi-threaded GUI applications Gdk.threads_init() must also be called prior to running
    Gtk.main() or Gio/Gtk.Application.run().
    """
    minor = Gtk.get_minor_version()
    micro = Gtk.get_micro_version()

    if minor == 10 and micro < 2:
        # Unfortunately these versions of PyGObject suffer a bug
        # which require a workaround to get threading working properly.
        # Workaround: Force GIL creation
        import threading
        threading.Thread(target=lambda: None).start()

    # Since version 3.10.2, calling threads_init is no longer needed.
    # See: https://wiki.gnome.org/PyGObject/Threading
    if minor < 10 or (minor == 10 and micro < 2):
        GObject.threads_init()
        # Gdk.threads_init()



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
