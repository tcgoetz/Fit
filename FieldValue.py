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
        return self.field.is_invalid(self.orig, self.invalid)

    def subfield_names(self):
        return self._subfield_names

    def type(self):
        return self.field.type

    def reconvert(self, measurement_system):
        (self.value, self.orig) = self.field.reconvert(self.orig, self.invalid, measurement_system)

    def units(self):
        return self.field.units(self.orig)

    def stats(self):
        return self.field.stats()

    def __getitem__(self, key):
        return self.__dict__[key]

    def __str__(self):
        field_string = self.field.name + "("
        if self.is_invalid():
            field_string += "[invalid]"
        else:
            field_string += repr(self.value)
        if self.units():
            field_string += " " + str(self.units())
        if self.value != self.orig:
            field_string += " (" + repr(self.orig) + ")"
        field_string += ")"
        return field_string

    def __repr__(self):
        return str(self)
