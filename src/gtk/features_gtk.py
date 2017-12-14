#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  features.py
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


ALL_FEATURES = ["a11y", "aur", "bluetooth", "cups", "chromium", "firefox", "firewall", "flash",
                "games", "graphic_drivers", "lamp", "lts", "office", "sshd", "visual", "vivaldi"]

# Not all desktops have all features
EXCLUDED_FEATURES = {
    'base': ["bluetooth", "chromium", "firefox", "firewall", "flash", "games",
             "graphic_drivers", "office", "visual", "vivaldi"],
    'cinnamon': ["lamp", "visual"],
    'deepin': ["lamp", "visual"],
    'gnome': ["lamp", "visual"],
    'kde': ["lamp", "visual"],
    'mate': ["lamp", "visual"],
    'openbox': ["lamp"],
    'xfce': ["lamp", "visual"],
    'budgie': ["lamp", "visual"],
    'enlightenment': ["lamp", "visual"],
    'i3': ["lamp"],
    'lxqt': ["lamp", "visual"]
}

ICON_NAMES = {
    'a11y': 'a11y',
    'aur': 'system-software-install',
    'bluetooth': 'bluetooth',
    'cups': 'printer',
    'chromium': 'chromium',
    'firefox': 'firefox',
    'vivaldi': 'vivaldi',
    'firewall': 'network-server',
    'flash': 'flash',
    'games': 'applications-games',
    'graphic_drivers': 'gnome-system',
    'lamp': 'applications-internet',
    'lts': 'applications-accessories',
    'office': 'accessories-text-editor',
    'sshd': 'network-connect',
    'visual': 'video-display'}


# See http://docs.python.org/2/library/gettext.html "22.1.3.4. Deferred translations"
def _(message):
    return message


TITLES = {
    'a11y': _("Adds accessibility packages"),
    'aur': _("Arch User Repository (AUR) Support"),
    'bluetooth': _("Bluetooth Support"),
    'cups': _("Printing Support"),
    'chromium': _("Chromium Web Browser"),
    'firefox': _("Firefox Web Browser"),
    'vivaldi': _("Vivaldi Web Browser"),
    'firewall': _("Uncomplicated Firewall"),
    'flash': _("Flash plugins"),
    'games': _("Steam + PlayonLinux"),
    'graphic_drivers': _("Graphic drivers (Proprietary)"),
    'lamp': _("Apache (or Nginx) + Mariadb + PHP"),
    'lts': _("Kernel (LTS version)"),
    'office': _("LibreOffice"),
    'sshd': _("SSH Service"),
    'visual': _("Visual Effects")}

DESCRIPTIONS = {
    'a11y': _("Useful packages for individuals who are blind or visually impaired."),
    'aur': _("The AUR is a community-driven repository for Arch users."),
    'bluetooth': _("Enables your system to make wireless connections via Bluetooth."),
    'chromium': _("Open-source web browser from Google."),
    'firefox': _("A popular open-source graphical web browser from Mozilla."),
    'vivaldi': _("Vivaldi is a free, fast web browser designed for power-users."),
    'flash': _("Freeware software normally used for multimedia."),
    'graphic_drivers': _("Installs AMD or Nvidia proprietary graphic driver."),
    'games': _("Installs Steam and Playonlinux for gaming enthusiasts."),
    'lamp': _("Apache (or Nginx) + Mariadb + PHP installation and setup."),
    'cups': _("Installation of printer drivers and management tools."),
    'office': _("Open source office suite. Supports editing MS Office files."),
    'visual': _("Enable transparency, shadows, and other desktop effects."),
    'firewall': _("Control the incoming and outgoing network traffic."),
    'sshd': _("Enables Secure SHell service."),
    'lts': _("Long term support (LTS) Linux kernel and modules.")}

TOOLTIPS = {
    'a11y': _("Useful packages for individuals who are blind or visually impaired."),
    'aur': _("Use yaourt to install AUR packages.\n"
             "The AUR was created to organize and share new packages\n"
             "from the community and to help expedite popular packages'\n"
             "inclusion into the [community] repository."),
    'bluetooth': _("Bluetooth is a standard for the short-range wireless\n"
                   "interconnection of cellular phones, computers, and\n"
                   "other electronic devices. In Linux, the canonical\n"
                   "implementation of the Bluetooth protocol stack is BlueZ."),
    'cups': _("CUPS is the standards-based, open source printing\n"
              "system developed by Apple Inc. for OS® X and other\n"
              "UNIX®-like operating systems."),
    'chromium': _("Chromium is an open-source browser project that aims to build a\n"
                  "safer, faster, and more stable way for all users to experience the web.\n"
                  "(this is the default)"),
    'firefox': _("Mozilla Firefox (known simply as Firefox) is a free and\n"
                 "open-source web browser developed for Windows, OS X, and Linux,\n"
                 "with a mobile version for Android, by the Mozilla Foundation and\n"
                 "its subsidiary, the Mozilla Corporation. Firefox uses the Gecko\n"
                 "layout engine to render web pages, which implements current and\n"
                 "anticipated web standards.  Enable this option to install Firefox\n"
                 "instead of Chromium"),
    'vivaldi': _("Vivaldi is a freeware, cross-platform web browser developed by\n"
                 "Vivaldi Technologies. It was officially launched on April 12, 2016.\n"
                 "The browser is aimed at staunch technologists, heavy Internet users,\n"
                 "and previous Opera web browser users disgruntled by Opera's transition\n"
                 "from the Presto layout engine to the Blink layout engine, which\n"
                 "removed many popular features."),
    'firewall': _("Ufw stands for Uncomplicated Firewall, and is a program for\n"
                  "managing a netfilter firewall. It provides a command line\n"
                  "interface and aims to be uncomplicated and easy to use."),
    'flash': _("Adobe Flash Player is freeware software for using content created\n"
               "on the Adobe Flash platform, including viewing multimedia, executing\n"
               "rich internet applications and streaming video and audio."),
    'games': _("Steam is one of the most popular gaming clients that supports\n"
               "linux in technology and gaming, while PlayOnLinux\n"
               "is a very easy manager to setting up games to play\n"
               "through wine, instead of doing it manually."),
    'graphic_drivers': _("Installs AMD or Nvidia proprietary graphics driver instead\n"
                         "of the open-source variant. Do NOT install this if you have a\n"
                         "Nvidia Optimus laptop"),
    'lamp': _("This option installs a web server (you can choose\n"
              "Apache or Nginx) plus a database server (Mariadb)\n"
              "and PHP."),
    'lts': _("The linux-lts package is an alternative Arch kernel package.\n"
             "This particular kernel version enjoys long-term support from upstream,\n"
             "including security fixes and some feature backports. Additionally, this\n"
             "package includes ext4 support. For Antergos users seeking a long-term\n"
             "support kernel, or who want a fallback kernel in case the latest kernel\n"
             "version causes problems, this option is the answer."),
    'office': _("LibreOffice is the free power-packed Open Source\n"
                "personal productivity suite for Windows, Macintosh\n"
                "and Linux, that gives you six feature-rich applications\n"
                "for all your document production and data processing\n"
                "needs: Writer, Calc, Impress, Draw, Math and Base."),
    'sshd': _("Secure Shell (SSH) is a network protocol that allows data to be\n"
              "exchanged over a secure channel between two computers.\n"
              "SSH is typically used to log into a remote machine and execute commands.\n"),
    'visual': _("Compton is a lightweight, standalone composite manager,\n"
                "suitable for use with window managers that do not natively\n"
                "provide compositing functionality. Compton itself is a fork\n"
                "of xcompmgr-dana, which in turn is a fork of xcompmgr.\n"
                "See the compton github page for further information.")}

# Delete previous _() dummy declaration
del _

""" Features screen """
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import subprocess
import logging

import misc.extra as misc

from pages.gtkbasebox import GtkBaseBox


class Graphics(object):
    def nvidia(self):
        from hardware.modules.nvidia import Nvidia
        if Nvidia().detect():
            return True
        from hardware.modules.nvidia_340xx import Nvidia340xx
        if Nvidia340xx().detect():
            return True
        from hardware.modules.nvidia_304xx import Nvidia304xx
        if Nvidia304xx().detect():
            return True
        return False

    def amd(self):
        from hardware.modules.catalyst import Catalyst
        return Catalyst().detect()

    def i915(self):
        from hardware.modules.i915 import Intel915
        return Intel915().detect()

    def bumblebee(self):
        return self.nvidia() and self.i915()


class Features(GtkBaseBox):
    """ Features screen class """

    COL_TITLE = 1
    COL_DESCRIPTION = 2
    COL_SWITCH = 3

    def __init__(self, params, prev_page="desktop", next_page="mirrors"):
        """ Initializes features ui """
        super().__init__(self, params, "features", prev_page, next_page)

        self.detect = Graphics()

        self.listbox_rows = {}

        self.a11y = params['a11y']

        # Set up list box
        self.listbox = self.ui.get_object("listbox")
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.listbox.set_sort_func(self.listbox_sort_by_name, None)

        # self.listbox.set_selection_mode(Gtk.SelectionMode.BROWSE)
        # self.listbox.connect("row-selected", self.on_listbox_row_selected)

        # This is initialized each time this screen is shown in prepare()
        self.features = None

        # Only show ufw rules and aur disclaimer info once
        self.info_already_shown = {"ufw": False, "aur": False}

        # Only load defaults for each DE the first time this screen is shown
        self.defaults_loaded = False

    @staticmethod
    def on_listbox_row_selected(listbox, listbox_row):
        """ Someone selected a different row of the listbox
            WARNING: IF LIST LAYOUT IS CHANGED THEN THIS SHOULD BE CHANGED ACCORDINGLY. """
        if listbox_row is not None:
            for vbox in listbox_row:
                switch = vbox.get_children()[2]
                if switch:
                    switch.set_active(not switch.get_active())

    def add_feature_icon(self, feature, box):
        """ Adds feature icon to listbox row box """
        if feature in ICON_NAMES:
            icon_name = ICON_NAMES[feature]
        else:
            logging.debug("No icon found for feature %s", feature)
            icon_name = "missing"

        image = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.DND)
        object_name = "image_" + feature
        image.set_name(object_name)
        image.set_property('margin_start', 10)
        self.listbox_rows[feature].append(image)
        box.pack_start(image, False, False, 0)

    def add_feature_label(self, feature, box):
        """ Adds feature title and label to listbox row box """
        text_box = Gtk.VBox()

        object_name = "label_title_" + feature
        label_title = Gtk.Label.new()
        label_title.set_halign(Gtk.Align.START)
        label_title.set_justify(Gtk.Justification.LEFT)
        label_title.set_name(object_name)
        self.listbox_rows[feature].append(label_title)
        text_box.pack_start(label_title, False, True, 0)

        object_name = "label_" + feature
        label = Gtk.Label.new()
        label.set_halign(Gtk.Align.START)
        label.set_justify(Gtk.Justification.LEFT)
        label.set_name(object_name)
        self.listbox_rows[feature].append(label)
        text_box.pack_start(label, False, False, 0)
        box.pack_start(text_box, False, False, 0)

    def on_switch_activated(self, switch, gparam):
        for feature in self.features:
            row = self.listbox_rows[feature]
            if row[Features.COL_SWITCH] == switch:
                is_active = switch.get_active()
                self.settings.set("feature_" + feature, is_active)

    def add_feature_switch(self, feature, box):
        object_name = "switch_" + feature
        switch = Gtk.Switch.new()
        switch.set_name(object_name)
        switch.set_property('margin_top', 10)
        switch.set_property('margin_bottom', 10)
        switch.set_property('margin_end', 10)
        switch.connect("notify::active", self.on_switch_activated)
        self.listbox_rows[feature].append(switch)
        box.pack_end(switch, False, False, 0)

    def fill_listbox(self):
        for listbox_row in self.listbox.get_children():
            listbox_row.destroy()

        self.listbox_rows = {}

        # Only add graphic-driver feature if an AMD or Nvidia is detected
        if "graphic_drivers" in self.features:
            allow = False
            if self.detect.amd():
                allow = True
            if self.detect.nvidia() and not self.detect.bumblebee():
                allow = True
            if not allow:
                logging.debug("Removing proprietary graphic drivers feature.")
                self.features.remove("graphic_drivers")

        for feature in self.features:
            box = Gtk.Box(spacing=20)
            box.set_name(feature + "-row")

            self.listbox_rows[feature] = []

            self.add_feature_icon(feature, box)
            self.add_feature_label(feature, box)
            self.add_feature_switch(feature, box)
            # Add row to our gtklist
            self.listbox.add(box)

        self.listbox.show_all()

    @staticmethod
    def listbox_sort_by_name(row1, row2, user_data):
        """ Sort function for listbox
            Returns : < 0 if row1 should be before row2, 0 if they are equal and > 0 otherwise
            WARNING: IF LAYOUT IS CHANGED IN fill_listbox THEN THIS SHOULD BE
            CHANGED ACCORDINGLY. """
        box1 = row1.get_child()
        txt_box1 = box1.get_children()[1]
        label1 = txt_box1.get_children()[0]

        box2 = row2.get_child()
        txt_box2 = box2.get_children()[1]
        label2 = txt_box2.get_children()[0]

        text = [label1.get_text(), label2.get_text()]
        # sorted_text = misc.sort_list(text, self.settings.get("locale"))
        sorted_text = misc.sort_list(text)

        # If strings are already well sorted return < 0
        if text[0] == sorted_text[0]:
            return -1

        # Strings must be swaped, return > 0
        return 1

    def set_row_text(self, feature, title, desc, tooltip):
        """ Set translated text to our listbox feature row """
        if feature in self.listbox_rows:
            title = "<span weight='bold' size='large'>{0}</span>".format(title)
            desc = "<span size='small'>{0}</span>".format(desc)
            row = self.listbox_rows[feature]
            row[Features.COL_TITLE].set_markup(title)
            row[Features.COL_DESCRIPTION].set_markup(desc)
            for widget in row:
                widget.set_tooltip_markup(tooltip)

    def translate_ui(self):
        """ Translates all ui elements """

        desktop = self.settings.get('desktop')
        txt = desktop + " - " + _("Feature Selection")
        self.header.set_subtitle(txt)

        for feature in self.features:
            title = _(TITLES[feature])
            desc = _(DESCRIPTIONS[feature])
            tooltip = _(TOOLTIPS[feature])
            self.set_row_text(feature, title, desc, tooltip)

        # Sort listbox items
        self.listbox.invalidate_sort()

    def switch_defaults_on(self):
        """ Enable some features by default """

        if 'bluetooth' in self.features:
            try:
                process1 = subprocess.Popen(["lsusb"], stdout=subprocess.PIPE)
                process2 = subprocess.Popen(
                    ["grep", "-i", "bluetooth"],
                    stdin=process1.stdout,
                    stdout=subprocess.PIPE)
                process1.stdout.close()
                out, process_error = process2.communicate()
                if out.decode() is not '':
                    row = self.listbox_rows['bluetooth']
                    row[Features.COL_SWITCH].set_active(True)
            except subprocess.CalledProcessError as err:
                logging.warning(
                    "Error checking bluetooth presence. Command %s failed: %s",
                    err.cmd,
                    err.output)

        if 'cups' in self.features:
            row = self.listbox_rows['cups']
            row[Features.COL_SWITCH].set_active(True)

        if 'visual' in self.features:
            row = self.listbox_rows['visual']
            row[Features.COL_SWITCH].set_active(True)

        if 'chromium' in self.features:
            row = self.listbox_rows['chromium']
            row[Features.COL_SWITCH].set_active(True)

        if 'a11y' in self.features and self.a11y:
            row = self.listbox_rows['a11y']
            row[Features.COL_SWITCH].set_active(True)

    def show_disclaimer_messages(self):
        """ Show ufw and AUR warning messages if necessary """
        # Show ufw info message if ufw is selected (show it only once)
        if self.settings.get("feature_firewall") and not self.info_already_shown["ufw"]:
            self.show_info_dialog("ufw")
            self.info_already_shown["ufw"] = True

        # Show AUR disclaimer if AUR is selected (show it only once)
        if self.settings.get("feature_aur") and not self.info_already_shown["aur"]:
            self.show_info_dialog("aur")
            self.info_already_shown["aur"] = True

    def show_info_dialog(self, feature):
        """ Some features show an information dialog when this screen is accepted """
        if feature == "aur":
            # Aur disclaimer
            txt1 = _("Arch User Repository - Disclaimer")
            txt2 = _("The Arch User Repository is a collection of user-submitted PKGBUILDs\n"
                     "that supplement software available from the official repositories.\n\n"
                     "The AUR is community driven and NOT supported by Arch or Antergos.\n")
        elif feature == "ufw":
            # Ufw rules info
            txt1 = _("Uncomplicated Firewall will be installed with these rules:")
            toallow = misc.get_network()
            txt2 = _("ufw default deny\nufw allow from {0}\nufw allow Transmission\n"
                     "ufw allow SSH").format(toallow)
        else:
            # No message
            return

        txt1 = "<big>{0}</big>".format(txt1)
        txt2 = "<i>{0}</i>".format(txt2)

        info = Gtk.MessageDialog(
            transient_for=self.get_main_window(),
            modal=True,
            destroy_with_parent=True,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.CLOSE)
        info.set_markup(txt1)
        info.format_secondary_markup(txt2)
        info.run()
        info.destroy()

    def ask_nginx(self):
        """ LAMP: Ask user if he wants Apache or Nginx """
        if self.settings.get("feature_lamp"):
            info = Gtk.MessageDialog(
                transient_for=self.get_main_window(),
                modal=True,
                destroy_with_parent=True,
                message_type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.YES_NO)
            info.set_markup("LAMP / LEMP")
            msg = _(
                "Do you want to install the Nginx server instead of the Apache server?")
            info.format_secondary_markup(msg)
            response = info.run()
            info.destroy()
            if response == Gtk.ResponseType.YES:
                self.settings.set("feature_lemp", True)
            else:
                self.settings.set("feature_lemp", False)

    def store_switches(self):
        """ Store current feature selections """
        for feature in self.features:
            row = self.listbox_rows[feature]
            is_active = row[Features.COL_SWITCH].get_active()
            self.settings.set("feature_" + feature, is_active)
            if is_active:
                logging.debug("Feature '%s' has been selected", feature)

    def store_values(self):
        """ Go to next screen, but first save changes """

        self.store_switches()
        self.show_disclaimer_messages()
        self.ask_nginx()

        self.listbox_rows = {}

        return True

    def prepare(self, direction):
        """ Prepare features screen to get ready to show itself """
        # Each desktop has its own features
        desktop = self.settings.get('desktop')
        self.features = list(
            set(ALL_FEATURES) -
            set(EXCLUDED_FEATURES[desktop]))
        self.fill_listbox()
        self.translate_ui()
        self.show_all()
        if not self.defaults_loaded:
            self.switch_defaults_on()
            # Only load defaults once
            self.defaults_loaded = True
        else:
            # Load values user has chosen when this screen is shown again
            self.load_values()

    def load_values(self):
        """ Get previous selected switches values """
        for feature in self.features:
            row = self.listbox_rows[feature]
            is_active = self.settings.get("feature_" + feature)
            if row[Features.COL_SWITCH] is not None and is_active is not None:
                row[Features.COL_SWITCH].set_active(is_active)


# When testing, no _() is available
try:
    _("")
except NameError as err:
    def _(message):
        return message

if __name__ == '__main__':
    from test_screen import _, run

    run('Features')
