"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.sport import Sport, SubSport, BoulderingFontGrade, IndoorFontGrade, PowerSaveTimeout, SportChange


class SportField(EnumField):
    """A field representing a sport via an ineger enum value."""

    _name = 'sport'
    _enum = Sport
    _units = {
        0 : 'cycles',
        1 : 'steps',
        2 : 'strokes',
        5 : 'strokes',
        11 : 'steps',
        15 : 'strokes',
        17 : 'steps',
        19 : 'strokes',
        37 : 'strokes',
    }

    @classmethod
    def units(cls, sport_index):
        """Return the proper units for an activity given the sport index."""
        try:
            return cls._units[sport_index]
        except Exception:
            return cls._units[0]


class SubSportField(EnumField):
    """A field representing a sub-sport via an ineger enum value."""

    _name = 'sub_sport'
    _enum = SubSport


#
# Climbing related fields
#
class BoulderingFontGradeField(EnumField):
    _name = 'grade'
    _enum = BoulderingFontGrade


class IndoorFontGradeField(EnumField):
    _name = 'grade'
    _enum = IndoorFontGrade


class PowerSaveTimeoutField(EnumField):
    _name = 'power_save_timeout'
    _enum = PowerSaveTimeout


class SportChangeField(EnumField):
    _name = 'sport_change'
    _enum = SportChange