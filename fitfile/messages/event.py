"""Structured data for decoding a FIT file event message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, TimestampField, IntegerField, EventField, EventTypeField, ActivityTypeField, RadarThreatLevelTypeField


event_message = {
    0 : EventField('event'),
    1 : EventTypeField(),
    2 : NamedField('data16'),
    3 : NamedField('data'),
    4 : NamedField('event_group'),
    #
    7 : IntegerField('score'),
    8 : IntegerField('opponent_score'),
    9 : NamedField('front_gear_num'),
    10 : NamedField('front_gear'),
    11 : NamedField('rear_gear_num'),
    12 : NamedField('rear_gear'),
    13 : IntegerField('device_index'),
    14 : ActivityTypeField(),
    15 : TimestampField('start_timestamp', utc=True),
    #
    21 : RadarThreatLevelTypeField(),
}
