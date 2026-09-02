"""Structured data for decoding a FIT file location message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import StringField, NamedField, LatiitudeField, LongitudeField, AltitudeField


location_message = {
    0 : StringField('name'),
    1 : LatiitudeField('position_lat'),
    2 : LongitudeField('position_long'),
    3 : NamedField('symbol'),
    4 : AltitudeField('altitude'),
    5 : AltitudeField('enhanced_altitude'),
    6 : StringField('description'),
}
