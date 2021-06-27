"""Objects that represent FIT file personal record message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .fields import Field, TimeMsField, PowerField, UnknownField, CaloriesField, TimeMinField
from .enum_fields import EnumField
from .object_fields import DistanceCentimetersToMetersField, AltitudeField
from .field_enums import PersonalRecordType, GoalType, GoalRecurrence, GoalSource


class PersonalRecordTypeField(EnumField):
    """Field that indicates what type of personal record the matching PersonalRecordField field holds."""

    _name = 'pr_type'
    _enum = PersonalRecordType


class PersonalRecordField(Field):
    """Field that holds a personal record."""

    _name = 'personal_record'
    _dependant_field_control_fields = ['pr_type']

    _type_to_fields = {
        PersonalRecordType.time         : TimeMsField,
        PersonalRecordType.distance     : DistanceCentimetersToMetersField,
        PersonalRecordType.elevation    : AltitudeField,
        PersonalRecordType.power        : PowerField
    }

    def dependant_field(self, control_value_list):
        """Return a field class that should be used to handle a dependant field."""
        pr_type = control_value_list[0]
        field_name = 'unknown_pr'
        if pr_type is not None:
            try:
                _dependant_field = self._type_to_fields[pr_type]
                field_name = pr_type.name
            except Exception:
                _dependant_field = UnknownField
        else:
            _dependant_field = Field
        return _dependant_field(field_name)


class GoalTypeField(EnumField):
    """Field that indicates what type of goal the matching GoalValueField field holds."""

    _name = 'goal_type'
    _enum = GoalType


class GoalRecurrenceField(EnumField):
    """Field that indicates how frequently the matching goal happens."""

    _name = 'goal_recurrence'
    _enum = GoalRecurrence


class GoalSourceField(EnumField):
    """A class that holds a field indicating what the source of a goal is as a enumeration."""

    _name = 'goal_source'
    _enum = GoalSource


class GoalValueField(Field):
    """Field that holds a goal value."""

    _name = 'target_value'
    _dependant_field_control_fields = ['type']

    _type_to_fields = {
        GoalType.time              : TimeMsField,
        GoalType.distance          : DistanceCentimetersToMetersField,
        GoalType.calories          : CaloriesField,
        GoalType.frequency         : Field,
        GoalType.steps             : Field,
        GoalType.ascent            : AltitudeField,
        GoalType.active_minutes    : TimeMinField
    }

    def dependant_field(self, control_value_list):
        """Return the dependant field class for this instance."""
        goal_type = control_value_list[0]
        field_name = 'unknown_goal'
        if goal_type is not None:
            try:
                _dependant_field = self._type_to_fields[goal_type]
                field_name = goal_type.name
            except Exception:
                _dependant_field = UnknownField
        else:
            _dependant_field = Field
        return _dependant_field(field_name)
