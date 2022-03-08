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

from bokeh.models.widgets import Select

class dropdown():

    def __init__(self, widget_lst, title, value, options, width, height):
        self.previous_label = ''
        self.title = title
        self.options = options
        self.value = value
        self.width = width
        self.height = height
        self.dropdown = None
        widget_lst.append(self)

    def initialize(self, widget_lst):
        if self.previous_label == '':
            label = self.value
            self.previous_label = self.value
        else:
            label = self.previous_label
        if self.width > 0 and self.height > 0:
            self.dropdown = Select(title = self.title, value = label,
                                      options = self.options, width = self.width, height = self.height)
        else:
            self.dropdown = Select(title = self.title, value = label,
                                      options = self.options)
        widget_lst.append(self.dropdown)
        if self.callback is not None:
            self.dropdown.on_change('value', self.callback,self.set_label)

    def add_callback(self, callback):
        self.callback = callback
        if self.dropdown is not None:
            self.dropdown.on_change('value', self.callback, self.set_label)
            
    def set_value(self, value):
        if self.dropdown is not None:
            self.dropdown.value = value
        self.value = value
        
    def set_label (self, attr, old, new):
        self.previous_label = new
