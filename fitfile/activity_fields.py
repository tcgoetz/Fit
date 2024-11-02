"""Objects that represent FIT file activity message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .fields import Field, NamedField, CyclesField, StepsField, StrokesField
from .enum_fields import EnumField
from .field_enums import Activity, ActivityType
from .sport import Sport, SubSport


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


class ActivityField(EnumField):
    """A field holding an activity as a integer enum value."""

    _name = 'activity'
    _enum = Activity


class ActivityTypeField(EnumField):
    """A field holding an activity type as a integer enum value."""

    _name = 'activity_type'
    _enum = ActivityType


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


class CadenceField(NamedField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'cadence'
    _units = 'rpm'


class StepsCadenceField(NamedField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'steps_per_min'
    _units = 'steps/min'


class StrokesCadenceField(NamedField):
    """Field that holds cycles/minute measurement for sports activity."""

    _name = 'strokes_per_min'
    _units = 'strokes/min'


def _cadence_sport_to_field(activity):
    _units = {
        'generic'                   : CadenceField,
        # steps activities
        'walking'                   : StepsCadenceField,
        'running'                   : StepsCadenceField,
        'hiking'                    : StepsCadenceField,
        'elliptical'                : StepsCadenceField,
        # strokes activities
        'cycling'                   : StrokesCadenceField,
        'swimming'                  : StrokesCadenceField,
        'rowing'                    : StrokesCadenceField,
        'paddling'                  : StrokesCadenceField,
        'stand_up_paddleboarding'   : StrokesCadenceField,
        'kayaking'                  : StrokesCadenceField,
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
        StrokesCadenceField: 1.0
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


class SportField(EnumField):
    """A field representing a sport via an ineger enum value."""

    _name = 'sport'
    _enum = Sport
    _units = {
        0 : 'cycles',
        1 : 'steps',
        2 : 'strokes',
        5 : 'strokes',
        11 : 'steps',
        15 : 'strokes',
        17 : 'steps',
        19 : 'strokes',
        37 : 'strokes',
    }

    @classmethod
    def units(cls, sport_index):
        """Return the proper units for an activity given the sport index."""
        try:
            return cls._units[sport_index]
        except Exception:
            return cls._units[0]


class SubSportField(EnumField):
    """A field representing a sub-sport via an ineger enum value."""

    _name = 'sub_sport'
    _enum = SubSport
