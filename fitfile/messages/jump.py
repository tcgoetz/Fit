"""Structured data for decoding a FIT file message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import DistanceMetersField, FloatField, LatiitudeField, LongitudeField, SpeedMpsField, IntegerField


jump_message = {
    0 : DistanceMetersField('distance'),
    1 : DistanceMetersField('height'),
    2 : IntegerField('rotations'),
    3 : FloatField('hang_time'),
    4 : FloatField('score'),
    5 : LatiitudeField('position_lat'),
    6 : LongitudeField('position_long'),
    7 : SpeedMpsField('speed'),
    8 : SpeedMpsField('speed'),
}
