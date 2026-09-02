"""Objects that represent FIT file activity message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from .field import Field, NamedField


class CaloriesField(NamedField):
    """A field containing a calories measurement in kcal."""

    _name = 'calories'
    _units = 'kcal'


class CaloriesDayField(NamedField):
    """A field containing a calories measurement for a day in kcal/day."""

    _units = 'kcal/day'


class CyclesCaloriesField(Field):

    _name = 'cycles_to_calories'
    _units = 'kcal/cycle'
    _scale = 5019.6
