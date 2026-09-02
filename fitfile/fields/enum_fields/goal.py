"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.goal import GoalType, GoalSource, GoalRecurrence, PersonalRecordType


class GoalTypeField(EnumField):
    """Field that indicates what type of goal the matching GoalValueField field holds."""

    _name = 'goal_type'
    _enum = GoalType


class GoalSourceField(EnumField):
    """A class that holds a field indicating what the source of a goal is as a enumeration."""

    _name = 'goal_source'
    _enum = GoalSource


class GoalRecurrenceField(EnumField):
    """Field that indicates how frequently the matching goal happens."""

    _name = 'goal_recurrence'
    _enum = GoalRecurrence


class PersonalRecordTypeField(EnumField):
    """Field that indicates what type of personal record the matching PersonalRecordField field holds."""

    _name = 'pr_type'
    _enum = PersonalRecordType
