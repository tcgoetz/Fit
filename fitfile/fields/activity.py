"""Objects that represent FIT file activity message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .field import Field, NamedField
from .types import BitField, FloatField
from .sport import CyclesField, StepsField, StrokesField
from .enum_fields.activity import ActivityTypeField


def _cycles_name_to_field(activity):
    field_mapping = {
        'generic'                   : CyclesField,
        # steps activities
        'walking'                   : StepsField,
        'running'                   : StepsField,
        'hiking'                    : StepsField,
        'elliptical'                : StepsField,
        # strokes activities
        'cycling'                   : StrokesField,
        'swimming'                  : StrokesField,
        'rowing'                    : StrokesField,
        'paddling'                  : StrokesField,
        'stand_up_paddleboarding'   : StrokesField,
        'kayaking'                  : StrokesField,
    }
    try:
        return field_mapping[activity.name]
    except Exception:
        return CyclesField


class ActivityBasedCyclesField(NamedField):
    """A cycles field that gnerates dependant fields based on the activity type."""

    _name = 'cycles'
    _units = 'cycles'
    _scale = 2.0
    _dependant_field_control_fields = ['activity_type']

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        activity_type = control_value_list[0]
        dependant_field = _cycles_name_to_field(activity_type)
        dependant_field_name = self.name.replace('cycles', dependant_field._units)
        return dependant_field(name=dependant_field_name)


class ActivityClassField(Field):
    """A field holding an activity class as a integer enum value."""

    _name = 'activity_class'

    def _convert_single(self, value, invalid):
        if value & 0x80:
            activity_class = "athlete "
        else:
            activity_class = ""
        activity_class += str(value & 0x7f)
        return activity_class


class IntensityField(Field):
    """A field that indicates how active the user was."""

    _name = 'intensity'
    _max_intensity = 8


class ActivityTypeIntensityField(NamedField):
    """A field that generates sub fields fields for activity and intensity."""

    activity_type_field = ActivityTypeField()
    intensity_field = IntensityField()

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def convert(self, value, invalid, measurement_system):
        """Convert the value to sub fields."""
        self.measurement_system = measurement_system
        activity_type = value & 0x1f
        intensity = value >> 5
        return self.activity_type_field.convert(activity_type, 0xff, measurement_system) + self.intensity_field.convert(intensity, 0xff, measurement_system)


class ActivityEvalEffort(Field):
    """Contains the users self evaluation of effort."""

    _name = 'self_eval_effort'

    @classmethod
    def get_self_eval_effort(cls, value):
        """Return the Garmin Connect self evaluation perceived effort label for the activity."""
        levels = [(100, "Maximum"), (90, "Extremely Hard"), (70, "Very Hard"), (50, "Hard"),
                  (40, "Somewhat Hard"), (30, "Moderate"), (20, "Light"), (10, "Very Light"), (0, "None")]
        for threshold, label in levels:
            if value >= threshold:
                return label

    def _convert_single(self, value, invalid):
        if value is not None and value != invalid:
            return self.get_self_eval_effort(value)


class ActivityEvalFeel(Field):
    """Contains the users self evaluation of how they felt."""

    _name = 'self_eval_feel'

    @classmethod
    def get_self_eval_feel(cls, value):
        """Return the Garmin'x self evaluation 'How did you feel' label for the activity."""
        levels = [(100, "Very Strong"), (75, "Strong"), (50, "Normal"), (25, "Weak"), (0, "Very Weak")]
        for threshold, label in levels:
            if value >= threshold:
                return label

    def _convert_single(self, value, invalid):
        if value is not None and value != invalid:
            return self.get_self_eval_feel(value)


class SportBasedCyclesField(NamedField):
    """A cycles field that generates dependant fields based on the sport type."""

    _units = 'cycles'
    _dependant_field_control_fields = ['sport', 'sub_sport']
    _scale_map = {
        CyclesField: 1.0,
        StepsField: 0.5,
        StrokesField: 1.0
    }

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        sport = control_value_list[0]
        dependant_field = _cycles_name_to_field(sport)
        if dependant_field._units == 'cycles':
            sub_sport = control_value_list[1]
            dependant_field = _cycles_name_to_field(sub_sport)
        dependant_field_name = self.name.replace('cycles', dependant_field._units)
        return dependant_field(name=dependant_field_name, scale=self._scale_map[dependant_field])


class CadenceField(FloatField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'cadence'
    _precision = 1
    _units = 'rpm'


class EnhancedCadenceField(FloatField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'cadence'
    _scale = 128
    _precision = 1
    _units = 'rpm'


class StepsCadenceField(NamedField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'steps_per_min'
    _units = 'steps/min'


class SwimStrokesCadenceField(NamedField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'strokes_per_min'
    _units = 'strokes/min'
    _scale = 10


def _cadence_sport_to_field(activity):
    _units = {
        'generic'                   : CadenceField,
        # steps activities
        'walking'                   : StepsCadenceField,
        'running'                   : StepsCadenceField,
        'hiking'                    : StepsCadenceField,
        'elliptical'                : StepsCadenceField,
        # strokes activities
        'cycling'                   : SwimStrokesCadenceField,
        'swimming'                  : SwimStrokesCadenceField,
        'rowing'                    : SwimStrokesCadenceField,
        'paddling'                  : SwimStrokesCadenceField,
        'stand_up_paddleboarding'   : SwimStrokesCadenceField,
        'kayaking'                  : SwimStrokesCadenceField,
    }
    try:
        return _units[activity.name]
    except Exception:
        return _units['generic']


class SportBasedCadenceField(CadenceField):
    """A cycles field that generates dependant fields based on the sport type."""

    _dependant_field_control_fields = ['sport', 'sub_sport']
    _scale_map = {
        CadenceField: 1.0,
        StepsCadenceField: 0.5,
        SwimStrokesCadenceField: 1.0
    }

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        sport = control_value_list[0]
        dependant_field = _cadence_sport_to_field(sport)
        if dependant_field._units == 'rpm':
            sub_sport = control_value_list[1]
            dependant_field = _cadence_sport_to_field(sub_sport)
        dependant_field_name = self.name.replace('cadence', dependant_field._name)
        return dependant_field(name=dependant_field_name, scale=self._scale_map[dependant_field])


class WorkField(Field):
    """A field that holds a work measurement in joules for an activity or portion of an activity."""

    _name = 'total_work'
    _units = 'J'


class WorkoutCapabilitiesField(BitField):
    """A filed that contains a mask of workout capabilities."""

    _name = 'workout_capabilities'
    _bits = {
        0x00000001: 'interval',
        0x00000002: 'custom',
        0x00000004: 'fitness_equipment',
        0x00000008: 'firstbeat',
        0x00000010: 'new_leaf',
        0x00000020: 'tcx',
        0x00000080: 'speed',
        0x00001000: 'grade',
        0x00002000: 'resistance',
        0x00008000: 'protected',
    }
