#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging


class OutputData():

    def __init__(self, files):
        self.files = files
        self.entries = []
        self.parse()

    def parse(self):
        for file in self.files:
            self.parse_messages(file)

    def field_names(self):
        return self.field_names_list

    def fields(self):
        return self.entries

    def __getitem__(self, index):
        return self.entries[index]
