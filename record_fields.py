"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field, TimeMsField, PowerField, UnknownField, CaloriesField, TimeMinField
from Fit.enum_fields import EnumField
from Fit.object_fields import DistanceCentimetersToMetersField, AltitudeField, EnhancedAltitudeField
import Fit.field_enums as fe


class PersonalRecordTypeField(EnumField):
    """Field that indicates what type of personal record the matching PersonalRecordField field holds."""

    enum = fe.PersonalRecordType

    def __init__(self):
        """Return a PersonalRecordTypeField instance."""
        super().__init__('pr_type')


class PersonalRecordField(Field):
    """Field that holds a personal record."""

    dependant_field_control_fields = ['pr_type']

    _type_to_fields = {
        fe.PersonalRecordType.time         : TimeMsField,
        fe.PersonalRecordType.distance     : DistanceCentimetersToMetersField,
        fe.PersonalRecordType.elevation    : AltitudeField,
        fe.PersonalRecordType.power        : PowerField
    }

    def __init__(self, *args, **kwargs):
        """Return a PersonalRecordField instance."""
        super().__init__(name='personal_record', *args, **kwargs)

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

    enum = fe.GoalType


class GoalRecurrenceField(EnumField):
    """Field that indicates how frequently the matching goal happens."""

    enum = fe.GoalRecurrence


class GoalSourceField(EnumField):
    """A class that holds a field indicating what the source of a goal is as a enumeration."""

    enum = fe.GoalSource


class GoalValueField(Field):
    """Field that holds a goal value."""

    dependant_field_control_fields = ['type']

    _type_to_fields = {
        fe.GoalType.time              : TimeMsField,
        fe.GoalType.distance          : DistanceCentimetersToMetersField,
        fe.GoalType.calories          : CaloriesField,
        fe.GoalType.frequency         : Field,
        fe.GoalType.steps             : Field,
        fe.GoalType.ascent            : EnhancedAltitudeField,
        fe.GoalType.active_minutes    : TimeMinField
    }

    def __init__(self, *args, **kwargs):
        """Return a GoalValueField instance."""
        super().__init__(name='target_value', *args, **kwargs)

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
