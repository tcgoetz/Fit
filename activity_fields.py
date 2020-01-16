"""Objects that represent FIT file activity message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field, NamedField, CyclesField, StepsField, StrokesField
from Fit.enum_fields import EnumField
import Fit.field_enums as fe
from Fit.sport import Sport, SubSport
from Fit.field_value import FieldValue


def _cycles_units_to_field(name):
    field_mapping = {
        'cycles' : CyclesField,
        'steps' : StepsField,
        'strokes' : StrokesField,
    }
    try:
        return field_mapping[name]
    except Exception:
        return CyclesField


def _cycles_activity_to_units(activity):
    _units = {
        'generic'                   : 'cycles',
        # steps activities
        'walking'                   : 'steps',
        'running'                   : 'steps',
        'hiking'                    : 'steps',
        'elliptical'                : 'steps',
        # strokes activities
        'cycling'                   : 'strokes',
        'swimming'                  : 'strokes',
        'rowing'                    : 'strokes',
        'paddling'                  : 'strokes',
        'stand_up_paddleboarding'   : 'strokes',
        'kayaking'                  : 'strokes',
    }
    try:
        return _units[activity.name]
    except Exception:
        return _units['generic']


class ActivityBasedCyclesField(NamedField):
    """A cycles field that gnerates dependant fields based on the activity type."""

    _name = 'cycles'
    _units = 'cycles'
    _scale = 2.0
    _dependant_field_control_fields = ['activity_type']

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        activity_type = control_value_list[0]
        dependant_field_name_base = _cycles_activity_to_units(activity_type)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return _cycles_units_to_field(dependant_field_name_base)(name=dependant_field_name)


class ActivityField(EnumField):
    """A field holding an activity as a integer enum value."""

    _name = 'activity'
    _enum = fe.Activity


class ActivityTypeField(Field):
    """A field holding an activity type as a integer enum value."""

    _name = 'activity_type'

    def _convert_single(self, value, invalid):
        return fe.ActivityType(value)

    def _convert_single_units(self, value, invalid):
        return _cycles_activity_to_units(fe.ActivityType(value).name)


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

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
        self._subfield['activity_type'] = ActivityTypeField()
        self._subfield['intensity'] = IntensityField()

    def convert(self, value, invalid, measurement_system):
        """Convert the value to sub fields."""
        self.measurement_system = measurement_system
        activity_type = value & 0x1f
        intensity = value >> 5
        return FieldValue(self, ['activity_type', 'intensity'],
                          invalid=invalid, value=self._convert_many(value, invalid), orig=value,
                          activity_type=self._subfield['activity_type'].convert(activity_type, 0xff, measurement_system),
                          intensity=self._subfield['intensity'].convert(intensity, 0xff, measurement_system))


class SportBasedCyclesField(NamedField):
    """A cycles field that generates dependant fields based on the sport type."""

    _units = 'cycles'
    _dependant_field_control_fields = ['sport', 'sub_sport']
    _scale_map = {
        'cycles'    : 1.0,
        'steps'     : 0.5,
        'strokes'   : 1.0
    }

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        sport = control_value_list[0]
        dependant_field_name_base = _cycles_activity_to_units(sport)
        if dependant_field_name_base == 'cycles':
            sub_sport = control_value_list[1]
            dependant_field_name_base = _cycles_activity_to_units(sub_sport)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return _cycles_units_to_field(dependant_field_name_base)(name=dependant_field_name, scale=self._scale_map[dependant_field_name_base])


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
