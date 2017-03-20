﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  features_info.py
#
#  Copyright © 2013-2016 Antergos
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


""" Features information """

# Note: As each desktop has its own features, these are listed
# in desktop_info file instead of here.

ICON_NAMES = {
    'aur': 'system-software-install',
    'bluetooth': 'bluetooth',
    'cups': 'printer',
    'chromium': 'chromium',
    'firefox': 'firefox',
    'firewall': 'network-server',
    'flash': 'flash',
    'games': 'applications-games',
    'graphic_drivers': 'gnome-system',
    'lamp': 'applications-internet',
    'lts': 'applications-accessories',
    'office': 'accessories-text-editor',
    'smb': 'gnome-mime-x-directory-smb-share',
    'visual': 'video-display'}


# See http://docs.python.org/2/library/gettext.html "22.1.3.4. Deferred translations"
def _(message):
    return message

TITLES = {
    'aur': _("Arch User Repository (AUR) Support"),
    'bluetooth': _("Bluetooth Support"),
    'cups': _("Printing Support"),
    'chromium': _("Chromium Web Browser"),
    'firefox': _("Firefox Web Browser"),
    'firewall': _("Uncomplicated Firewall"),
    'flash': _("Flash plugins"),
    'games': _("Steam + PlayonLinux"),
    'graphic_drivers': _("Graphic drivers (Proprietary)"),
    'lamp': _("Apache (or Nginx) + Mariadb + PHP"),
    'lts': _("Kernel (LTS version)"),
    'office': _("LibreOffice"),
    'smb': _("Windows sharing SMB"),
    'visual': _("Visual Effects")}

DESCRIPTIONS = {
    'aur': _("The AUR is a community-driven repository for Arch users."),
    'bluetooth': _("Enables your system to make wireless connections via Bluetooth."),
    'chromium': _("Open-source web browser from Google."),
    'firefox': _("A popular open-source graphical web browser from Mozilla."),
    'flash': _("Freeware software normally used for multimedia."),
    'graphic_drivers': _("Installs AMD or Nvidia proprietary graphic driver."),
    'games': _("Installs Steam and Playonlinux for gaming enthusiasts."),
    'lamp': _("Apache (or Nginx) + Mariadb + PHP installation and setup."),
    'cups': _("Installation of printer drivers and management tools."),
    'office': _("Open source office suite. Supports editing MS Office files."),
    'visual': _("Enable transparency, shadows, and other desktop effects."),
    'firewall': _("Control the incoming and outgoing network traffic."),
    'lts': _("Long term support (LTS) Linux kernel and modules."),
    'smb': _("Provides client access to shared files and printers.")}

TOOLTIPS = {
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
    'smb': _("Most usage of SMB involves computers running Microsoft Windows.\n"
             "Use this option to be able to browse SMB shares from your computer."),
    'visual': _("Compton is a lightweight, standalone composite manager,\n"
                "suitable for use with window managers that do not natively\n"
                "provide compositing functionality. Compton itself is a fork\n"
                "of xcompmgr-dana, which in turn is a fork of xcompmgr.\n"
                "See the compton github page for further information.")}

# Delete previous _() dummy declaration
del _
