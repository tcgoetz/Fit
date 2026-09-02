"""Structured data for decoding a FIT file split message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimeMsField, TimestampField, DistanceMetersField, HeartRateField, FloatField, CaloriesField, ClimbingGrade, ClimbingRouteComleted, IntegerField


split_message = {
    1  : TimeMsField('total_elapsed_time'),
    2  : TimeMsField('total_timer_time'),
    4  : TimestampField('start_time', utc=True),
    5  : TimestampField('end_time', utc=True),
    13 : DistanceMetersField('ascent'),
    14 : DistanceMetersField('descent'),
    15 : HeartRateField('avg_heart_rate'),
    16 : HeartRateField('max_heart_rate'),
    26 : FloatField('avg_vertical_speed'),
    28 : CaloriesField('total_calories'),
    70 : ClimbingGrade('grade'),
    71 : ClimbingRouteComleted('completed'),
    72 : IntegerField('falls'),
}
