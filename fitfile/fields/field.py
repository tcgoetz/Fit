"""Objects that represent FIT file message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..measurement import MeasurementSystem
from ..field_value import FieldValue


class Field():
    """The base object for all FIT file message fields."""

    _name = None
    _units = None
    _scale = 1.0
    _offset = 0.0
    _dependant_field_control_fields = None

    def __init__(self, **kwargs):
        """Return a new instance of the Field class."""
        for key, value in kwargs.items():
            vars(self)['_' + key] = value
        if self._name is None:
            raise ValueError(f'Unamed instance of {self.__class__.__name__}')

    @property
    def name(self):
        """Return the name of the field."""
        return self._name

    @property
    def units(self):
        """Return the units of the field."""
        return self._units

    def _invalid_single(self, value, invalid):
        return (value == invalid)

    def _invalid_many(self, values, invalid):
        for value in values:
            if self._invalid_single(value, invalid):
                return True
        return False

    def is_invalid(self, value, invalid):
        """Return if the field's value is valid."""
        if isinstance(value, list):
            return self._invalid_many(value, invalid)
        return self._invalid_single(value, invalid)

    def _convert_single(self, value, invalid):
        if value is not None and value != invalid:
            return (value / self._scale) + self._offset

    def __convert_many(self, _convert_single, value, invalid):
        if isinstance(value, list):
            return [_convert_single(sub_value, invalid) for sub_value in value]
        return _convert_single(value, invalid)

    def _convert_many(self, value, invalid):
        return self.__convert_many(self._convert_single, value, invalid)

    def convert(self, value, invalid, measurement_system=MeasurementSystem.metric):
        """Return a FieldValue as intepretted by the field's rules."""
        self.measurement_system = measurement_system
        return [FieldValue(self, value, invalid, **{self._name: self._convert_many(value, invalid)})]

    def reconvert(self, value, invalid, measurement_system=MeasurementSystem.metric):
        """Return the field's value as intepretted by the field's rules."""
        self.measurement_system = measurement_system
        return {self._name: self._convert_many(value, invalid)}

    def __repr__(self):
        """Return a string representation of a Field instance."""
        return f'{self.__class__.__name__} ({self._name})'


class NamedField(Field):
    """A field with a name that is passed to the constructor."""

    def __init__(self, *args, **kwargs):
        """Return an NamedField instance."""
        if len(args) > 0:
            super().__init__(name=args[0], **kwargs)
        else:
            super().__init__(**kwargs)


#
# Special fields
#
class UnknownField(Field):
    """Class that handles fields that are not documented."""

    def __init__(self, index):
        """Return a new instance of the UnknownField class."""
        super().__init__(name=f"unknown_{index}")


#
# Basic field types
#
class LeftRightBalanceField(NamedField):
    """A composite field that indicates left or roight and the percentage for that side."""

    def _convert_single(self, value, invalid):
        if value != invalid:
            if value & 0x8000:
                left_or_right = 'Right'
            else:
                left_or_right = 'Left'
            percentage = (value & 0x3fff) / 100
            return f'{left_or_right} {percentage} %'


class PercentField(NamedField):
    """A field holding a integer percentage value."""

    _units = '%'
    _scale = 100.0


class BytePercentField(PercentField):
    """A field holding a integer percentage value."""

    _scale = 2.0


class MessageIndexField(NamedField):

    def _convert_single(self, value, invalid):
        return {'selected': ((value & 0x8000) == 0x8000), 'value': (value & 0x0FFF)}


class VersionField(NamedField):
    """A field that contains a software or hardware version."""

    _name = 'version'
    _scale = 100.0

    def _convert_single(self, value, invalid):
        if value != invalid:
            return '{0:2.2f}'.format(value / self._scale)
