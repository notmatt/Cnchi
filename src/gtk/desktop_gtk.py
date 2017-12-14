#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  desktop.py
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


""" Desktop screen """

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
import os
import logging


from pages.gtkbasebox import GtkBaseBox

import misc.extra as misc


DESKTOPS = ["base", "cinnamon", "deepin",
            "gnome", "kde", "mate", "openbox", "xfce"]

DESKTOPS_DEV = DESKTOPS + ["budgie", "enlightenment", "i3", "lxqt"]

DESKTOPS_A11Y = ["gnome", "mate"]

DESKTOP_ICONS_PATH = "/usr/share/cnchi/data/icons"

'''
MENU - Size appropriate for menus (16px).
SMALL_TOOLBAR - Size appropriate for small toolbars (16px).
LARGE_TOOLBAR - Size appropriate for large toolbars (24px)
BUTTON - Size appropriate for buttons (16px)
DND - Size appropriate for drag and drop (32px)
DIALOG - Size appropriate for dialogs (48px)
'''

# Descriptive names
NAMES = {
    'base': "Base",
    'cinnamon': "Cinnamon",
    'deepin': "Deepin",
    'gnome': "GNOME",
    'kde': "KDE",
    'mate': "MATE",
    'openbox': "Openbox",
    'xfce': "Xfce",
    'budgie': "Budgie",
    'enlightenment': "Enlightenment",
    'i3': "i3",
    'lxqt': "LXQt"
}

LIBS = {
    'gtk': ["cinnamon", "deepin", "gnome", "mate", "openbox", "xfce", "budgie", "enlightenment", "i3"],
    'qt': ["kde", "lxqt"]
}

# Session names for lightDM setup (/usr/share/xsessions)
SESSIONS = {
    'cinnamon': 'cinnamon',
    'deepin': 'deepin',
    'gnome': 'gnome',
    'kde': 'plasma',
    'mate': 'mate',
    'openbox': 'openbox',
    'xfce': 'xfce',
    'budgie': 'budgie-desktop',
    'enlightenment': 'enlightenment',
    'i3': 'i3',
    'lxqt': 'lxsession'
}


# See http://docs.python.org/2/library/gettext.html "22.1.3.4. Deferred translations"
def _(message):
    return message


DESCRIPTIONS = {
    'base':     _("This option will install Antergos as command-line only system, "
                  "without any type of graphical interface. After the installation "
                  "you can customize Antergos by installing packages with the "
                  "command-line package manager."),

    'cinnamon': _("Cinnamon is a Linux desktop which provides advanced, "
                  "innovative features and a traditional desktop user experience. "
                  "Cinnamon aims to make users feel at home by providing them with "
                  "an easy-to-use and comfortable desktop experience."),

    'deepin':   _("Deepin desktop is a lightweight, elegant desktop environment. "
                  "It was originally created for Linux Deepin distribution. Now, "
                  "DDE will support most Linux operating systems such as Arch Linux, "
                  "Ubuntu, Fedora, openSUSE etc."),

    'gnome':    _("GNOME 3 is an easy and elegant way to use your computer. "
                  "It features the Activities Overview which is an easy way to "
                  "access all your basic tasks."),

    'kde':      _("If you are looking for a familiar working environment, KDE's "
                  "Plasma Desktop offers all the tools required for a modern desktop "
                  "computing experience so you can be productive right from the start."),

    'mate':     _("MATE is an intuitive, attractive, and lightweight desktop "
                  "environment which provides a more traditional desktop "
                  "experience. Accelerated compositing is supported, but not "
                  "required to run MATE making it suitable for lower-end hardware."),

    'openbox':  _("Not actually a desktop environment, Openbox is a highly "
                  "configurable window manager. It is known for its "
                  "minimalistic appearance and its flexibility. It is the most "
                  "lightweight graphical option offered by antergos. Please "
                  "Note: Openbox is not recommended for users who are new to Linux."),

    'xfce':     _("Xfce is a lightweight desktop environment. It aims to "
                  "be fast and low on system resources, while remaining visually "
                  "appealing and user friendly. It suitable for use on older "
                  "computers and those with lower-end hardware specifications. "),

    'budgie':   _("Budgie is the flagship desktop of Solus and is a Solus project. "
                  "It focuses on simplicity and elegance. Written from scratch with "
                  "integration in mind, the Budgie desktop tightly integrates with "
                  "the GNOME stack, but offers an alternative desktop experience."),

    'enlightenment': _("Enlightenment is not just a window manager for Linux/X11 "
                       "and others, but also a whole suite of libraries to help "
                       "you create beautiful user interfaces with much less work"),

    'i3':       _("i3 is a tiling window manager, completely written from scratch. "
                  "The target platforms are GNU/Linux and BSD operating systems, "
                  "its code is Free and Open Source Software (FOSS) under the BSD "
                  "license. i3 is primarily targeted at advanced users and developers."),

    'lxqt':     _("LXQt is the next-generation of LXDE, the Lightweight Desktop "
                  "Environment. It is lightweight, modular, blazing-fast, and "
                  "user-friendly.")
}

# Delete previous _() dummy declaration
del _

class DesktopAsk(GtkBaseBox):
    """ Class to show the Desktop screen """

    def __init__(self, params, prev_page="keymap", next_page="features"):
        super().__init__(self, params, "desktop", prev_page, next_page)

        data_dir = self.settings.get('data')
        self.desktops_dir = os.path.join(data_dir, "images", "desktops")

        self.desktop_info = self.ui.get_object("desktop_info")

        self.desktop_image = None
        self.icon_desktop_image = None

        # Set up list box
        self.listbox = self.ui.get_object("listbox_desktop")
        self.listbox.connect("row-selected", self.on_listbox_row_selected)
        self.listbox.set_selection_mode(Gtk.SelectionMode.BROWSE)
        self.listbox.set_sort_func(self.listbox_sort_by_name, None)

        self.desktop_choice = 'gnome'

        self.enabled_desktops = self.settings.get("desktops")

        self.set_desktop_list()

    def translate_ui(self, desktop, set_header=True):
        """ Translates all ui elements """
        label = self.ui.get_object("desktop_info")
        txt = "<span weight='bold'>{0}</span>\n".format(NAMES[desktop])
        description = DESCRIPTIONS[desktop]
        txt = txt + _(description)
        label.set_markup(txt)

        # This sets the desktop's image
        path = os.path.join(self.desktops_dir, desktop + ".png")
        if self.desktop_image is None:
            self.desktop_image = Gtk.Image.new_from_file(path)
            overlay = self.ui.get_object("image_overlay")
            overlay.add(self.desktop_image)
        else:
            self.desktop_image.set_from_file(path)

        # and this sets the icon
        filename = "desktop-environment-" + desktop.lower() + ".svg"
        icon_path = os.path.join(DESKTOP_ICONS_PATH, "scalable", filename)
        icon_exists = os.path.exists(icon_path)

        if self.icon_desktop_image is None:
            if icon_exists:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                    icon_path, 48, 48)
                self.icon_desktop_image = Gtk.Image.new_from_pixbuf(pixbuf)
            else:
                filename = desktop.lower() + ".png"
                icon_path = os.path.join(DESKTOP_ICONS_PATH, "48x48", filename)
                icon_exists = os.path.exists(icon_path)
                if icon_exists:
                    self.icon_desktop_image = Gtk.Image.new_from_file(
                        icon_path)
                else:
                    self.icon_desktop_image = Gtk.Image.new_from_icon_name(
                        "image-missing",
                        Gtk.IconSize.DIALOG)

            overlay = self.ui.get_object("image_overlay")
            overlay.add_overlay(self.icon_desktop_image)
        else:
            if icon_exists:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                    icon_path, 48, 48)
                self.icon_desktop_image.set_from_pixbuf(pixbuf)
            else:
                filename = desktop.lower() + ".png"
                icon_path = os.path.join(DESKTOP_ICONS_PATH, "48x48", filename)
                icon_exists = os.path.exists(icon_path)
                if icon_exists:
                    self.icon_desktop_image.set_from_file(icon_path)
                else:
                    self.icon_desktop_image.set_from_icon_name(
                        "image-missing", Gtk.IconSize.DIALOG)

        if set_header:
            # set header text
            txt = _("Choose Your Desktop")
            self.header.set_subtitle(txt)

    def prepare(self, direction):
        """ Prepare screen """
        self.translate_ui(self.desktop_choice)
        self.show_all()

    def set_desktop_list(self):
        """ Set desktop list in the ListBox """
        for desktop in sorted(NAMES):
            if desktop in self.enabled_desktops:
                box = Gtk.HBox()

                filename = "desktop-environment-" + desktop.lower() + ".svg"
                icon_path = os.path.join(DESKTOP_ICONS_PATH, "scalable", filename)
                if os.path.exists(icon_path):
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                        icon_path, 24, 24)
                    image = Gtk.Image.new_from_pixbuf(pixbuf)
                else:
                    filename = desktop.lower() + ".png"
                    icon_path = os.path.join(DESKTOP_ICONS_PATH, "24x24", filename)
                    if os.path.exists(icon_path):
                        image = Gtk.Image.new_from_file(icon_path)
                    else:
                        image = Gtk.Image.new_from_icon_name(
                            "image-missing",
                            Gtk.IconSize.LARGE_TOOLBAR)
                box.pack_start(image, False, False, 2)

                label = Gtk.Label()
                label.set_markup(NAMES[desktop])
                box.pack_start(label, False, False, 2)

                self.listbox.add(box)

        # Set Gnome as default
        self.select_default_row(NAMES["gnome"])

    @staticmethod
    def listbox_sort_by_name(row1, row2, user_data):
        """ Sort function for listbox
            Returns : < 0 if row1 should be before row2, 0 if they are equal and > 0 otherwise
            WARNING: IF LAYOUT IS CHANGED IN fill_listbox THEN THIS SHOULD BE
            CHANGED ACCORDINGLY. """
        box1 = row1.get_child()
        label1 = box1.get_children()[1]

        box2 = row2.get_child()
        label2 = box2.get_children()[1]

        text = [label1.get_text(), label2.get_text()]
        # sorted_text = misc.sort_list(text, self.settings.get("locale"))
        sorted_text = misc.sort_list(text)

        # If strings are already well sorted return < 0
        if text[0] == sorted_text[0]:
            return -1

        # Strings must be swaped, return > 0
        return 1

    def select_default_row(self, desktop_name):
        """ Selects default row
            WARNING: IF LAYOUT IS CHANGED IN desktop.ui THEN THIS SHOULD BE
            CHANGED ACCORDINGLY. """
        for listbox_row in self.listbox.get_children():
            for vbox in listbox_row.get_children():
                label = vbox.get_children()[1]
                if desktop_name == label.get_text():
                    self.listbox.select_row(listbox_row)
                    return

    def set_desktop(self, desktop):
        """ Show desktop info """
        for key in NAMES.keys():
            if NAMES[key] == desktop:
                self.desktop_choice = key
                self.translate_ui(self.desktop_choice, set_header=False)
                return

    def on_listbox_row_selected(self, listbox, listbox_row):
        """ Someone selected a different row of the listbox
            WARNING: IF LAYOUT IS CHANGED IN desktop.ui THEN THIS SHOULD BE
            CHANGED ACCORDINGLY. """
        if listbox_row is not None:
            for vbox in listbox_row:
                label = vbox.get_children()[1]
                desktop = label.get_text()
                self.set_desktop(desktop)

    def store_values(self):
        """ Store desktop """
        self.settings.set('desktop', self.desktop_choice.lower())
        logging.info(
            "Cnchi will install Antergos with the '%s' desktop",
            self.desktop_choice.lower())
        return True

    @staticmethod
    def scroll_to_cell(treeview, path):
        """ Scrolls treeview to show the desired cell """
        treeview.scroll_to_cell(path)
        return False


# When testing, no _() is available
try:
    _("")
except NameError as err:
    def _(message):
        return message

if __name__ == '__main__':
    from test_screen import _, run

    run('DesktopAsk')
