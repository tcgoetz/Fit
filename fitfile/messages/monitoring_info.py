"""Structured data for decoding a FIT file location message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import TimestampField, ActivityTypeField, CyclesDistanceField, CyclesCaloriesField, CaloriesDayField, CyclesField


monitoring_info_message = {
    0 : TimestampField('local_timestamp', utc=False),
    1 : ActivityTypeField(),
    #
    3 : CyclesDistanceField(),
    4 : CyclesCaloriesField(),
    5 : CaloriesDayField('resting_metabolic_rate'),
    #
    7 : CyclesField('cycles_goal')
}
