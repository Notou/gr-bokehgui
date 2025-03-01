# Copyright 2017 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

from bokeh.models.widgets import CheckboxGroup

class checkbox():
    def __init__(self, widget_lst, default_value, label, inline = True):
        self.label = label
        self.default_value = default_value
        self.inline = inline
        self.checkbox = None
        self.callback = None
        # self.initialize(default_value, label, inline)
        widget_lst.append(self)

    def initialize(self, widget_lst):
        self.checkbox = CheckboxGroup(active = self.default_value, labels = [self.label],
                                      inline = self.inline)
        widget_lst.append(self.checkbox)
        if self.callback is not None:
            self.checkbox.on_change('active', self.callback)

    def add_callback(self, callback):
        self.callback = callback
        if self.checkbox is not None:
            self.checkbox.on_change('active', self.callback)
