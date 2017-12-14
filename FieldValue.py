#!/usr/bin/env python

#
# copyright Tom Goetz
#


class FieldValue():
    def __init__(self, field, subfield_names=None, **kwargs):
        self.field = field
        self._subfield_names = subfield_names

        self._value = {}
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                self._value[key] = value

    def invalid(self):
        return (self['value'] == self['invalid'])

    def name(self):
        return self.field.name

    def subfield_names(self):
        return self._subfield_names

    def type(self):
        return self.field.type

    def value(self):
        return self['value']

    def reconvert(self):
        self._value['value'] = self.field.convert_many(self._value['orig'])

    def units(self):
        return self.field.units(self['orig'])

    def stats(self):
        return self.field.stats()

    def __getitem__(self, name):
        return self._value[name]

    def __iter__(self):
        return iter(self._value)

    def keys(self):
        return self._value.keys()

    def items(self):
        return self._value.items()

    def values(self):
        return self._value.values()

    def __str__(self):
        field_string = self.name() + " " + str(self['value'])
        if self.units():
            field_string += " " + str(self.units())
        field_string += " (" + str(self['orig']) + ")"
        if self.invalid():
            field_string += " [invalid]"
        return field_string

    def __repr__(self):
        return self.__str__()