"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.user_profile import DisplayHeart, DisplayOrientation, DisplayPosition, Gender, Language
from ...measurement import MeasurementSystem


class GenderField(EnumField):
    """A FIT file message field containing the user's gender."""

    _name = 'gender'
    _enum = Gender


class DisplayHeartField(EnumField):

    _enum = DisplayHeart


class DisplayMeasureField(EnumField):

    _enum = MeasurementSystem


class DisplayOrientationField(EnumField):
    """A Field that holds the display orientation setting for the device."""

    _name = 'display_orientation'
    _enum = DisplayOrientation


class DisplayPositionField(EnumField):

    _name = 'position_setting'
    _enum = DisplayPosition


class LanguageField(EnumField):
    """A FIT file message field containing the user's language."""

    _name = 'language'
    _enum = Language
