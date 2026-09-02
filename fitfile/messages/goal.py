"""Structured data for decoding a FIT file goal message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import BoolField, NamedField, TimestampField, SportField, SubSportField, GoalTypeField, GoalValueField, GoalRecurrenceField, GoalSourceField


goal_message = {
    0 : SportField(),
    1 : SubSportField(),
    2 : TimestampField('start_time', utc=True),
    3 : TimestampField('end_time', utc=True),
    4 : GoalTypeField('type'),
    5 : NamedField('value'),
    6 : BoolField('repeat'),
    7 : GoalValueField(),
    8 : GoalRecurrenceField('recurrence'),
    9 : NamedField('recurrence_value'),
    10 : BoolField('enabled'),
    11 : GoalSourceField('source')
}
