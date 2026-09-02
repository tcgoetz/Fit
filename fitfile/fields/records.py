"""Objects that represent FIT file personal record message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .field import Field, UnknownField
from .calories import CaloriesField
from .time import TimeMsField, TimeMinField
from .sport import PowerField
from .field_enums.goal import PersonalRecordType, GoalType
from .objects import DistanceCentimetersToMetersField, AltitudeField


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
