"""Structured data for decoding a FIT file climb pro message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import LatiitudeField, LongitudeField, IntegerField, ClimbProEventField, DistanceMetersField


climb_pro_message = {
    0 : LatiitudeField('position_lat'),
    1 : LongitudeField('position_long'),
    2 : ClimbProEventField('climb_pro_event'),
    3 : IntegerField('climb_number'),
    4 : IntegerField('climb_category'),
    5 : DistanceMetersField('current_dist')
}
