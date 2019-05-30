#!/usr/bin/env python

#
# copyright Tom Goetz
#


class FieldValue(object):
    def __init__(self, field, subfield_names=None, **kwargs):
        self.field = field
        self._subfield_names = subfield_names

        self.__dict__.update(kwargs)

    def is_invalid(self):
        return (self.orig == self.invalid)

    def subfield_names(self):
        return self._subfield_names

    def type(self):
        return self.field.type

    def reconvert(self):
        self.value = self.field.convert_many(self.orig, self.invalid)

    def units(self):
        return self.field.units(self.orig)

    def stats(self):
        return self.field.stats()

    def __getitem__(self, key):
        return self.__dict__[key]

    def __str__(self):
        field_string = self.field.name + "(" + repr(self.value)
        if self.units():
            field_string += " " + str(self.units())
        if self.value != self.orig:
            field_string += " (" + repr(self.orig) + ")"
        if self.is_invalid():
            field_string += " [invalid]"
        field_string += ")"
        return field_string

    def __repr__(self):
        return str(self)
