"""Structured data for decoding a FIT file totals message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeSField, CaloriesField, IntegerField, StringField, SportField, DistanceMetersField


totals_message = {
    0 : TimeSField('timer_time'),
    1 : DistanceMetersField('distance'),
    2 : CaloriesField(),
    3 : SportField(),
    4 : TimeSField('elapsed_time'),
    5 : IntegerField('sessions'),
    6 : TimeSField('active_time'),
    9 : IntegerField('sport_index'),
    10 : StringField('activity_profile'),
}
