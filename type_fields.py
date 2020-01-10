"""Objects that represent FIT file device message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field, NamedField


class TypeField(NamedField):
    """A base class for fields based on python types."""

    def __init__(self, type_func, *args, **kwargs):
        """Return a field instance that holds an type. Convert to the type using type_func."""
        self.type_func = type_func
        super().__init__(*args, **kwargs)

    def _convert_single(self, value, invalid):
        if value != invalid:
            try:
                return self.type_func(value / self._scale)
            except Exception:
                return value


class ScaledTypeField(TypeField):
    """A base class for fields based on python types."""

    def _convert_single(self, value, invalid):
        if value != invalid:
            try:
                return self.type_func(value / self._scale)
            except Exception:
                return value


class IntegerField(ScaledTypeField):
    """A FIT file message field with a integer value."""

    def __init__(self, *args, **kwargs):
        """Return a field instance that holds an integer."""
        super().__init__(int, *args, **kwargs)


class FloatField(ScaledTypeField):
    """A FIT file message field with a float value."""

    def __init__(self, *args, **kwargs):
        super().__init__(float, *args, **kwargs)


class BoolField(TypeField):
    """A FIT file message field with a boolean value."""

    def __init__(self, *args, **kwargs):
        super().__init__(bool, *args, **kwargs)


class BitField(Field):
    """A FIT file message field with a bitfield value."""

    def _convert_single(self, value, invalid):
        if value != invalid:
            return self._bits.get(value, [self._bits[bit] for bit in self._bits if ((bit & value) == bit)])


class StringField(NamedField):
    """A FIT file message field with a string value."""

    def _invalid_single(self, value, invalid):
        return (value < 0) or (value > 127)

    def _convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = ""
            for aschii_index in value:
                if aschii_index == 0:
                    break
                converted_value += chr(aschii_index)
        else:
            converted_value = str(value)
        return converted_value.strip()


class BytesField(NamedField):
    """A FIT file message field with a bytearray value."""

    def _convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = bytearray()
            for character in value:
                converted_value.append(character)
        else:
            converted_value = bytearray(value)
        return converted_value


class HeartRateField(FloatField):
    """A FIT file message field holding a heart rate measurement."""

    _units = 'bpm'


class AbsolutePressureField(IntegerField):
    """Absolute pressure measure for diving?."""

    _name = 'absolute_pressure'
    _units = 'Pa'


class RespirationRateField(FloatField):
    """A respiration rate measurment in breaths per minute."""

    _name = 'respiration_rate'
    _units = 'brpm'
    _scale = 100.0
