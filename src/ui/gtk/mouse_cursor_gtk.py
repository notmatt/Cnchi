#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#  Copyright (c) 2013-2017 Antergos
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import logging

from gi.repository import Gtk, Gdk


def gtk_refresh():
    """ Tell Gtk loop to run pending events """
    while Gtk.events_pending():
        Gtk.main_iteration()

def set_cursor(window, cursor_type):
    """ Set mouse cursor """
    try:
        if window:
            display = Gdk.Display.get_default()
            cursor = Gdk.Cursor.new_for_display(display, cursor_type)
            window.set_cursor(cursor)
            gtk_refresh()
    except Exception as ex:
        logging.debug(ex)

def set_cursor(cursor_type):
    """ Set mouse cursor """
    try:
        screen = Gdk.Screen.get_default()
        window = Gdk.Screen.get_root_window(screen)

        set_cursor(window, cursor_type)
    except Exception as ex:
        logging.debug(ex)
