"""Objects that represent FIT file sport message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .field import Field, NamedField
from .types import FloatField
from .enum_fields.sport import Sport, SubSport, BoulderingFontGradeField, IndoorFontGradeField


class CyclesField(Field):
    """Field that holds cycles measurement for sports activity."""

    _name = 'cycles'
    _units = 'cycles'
    _scale = 2.0


class StepsField(Field):
    """Field that holds steps measurement for sports activity."""

    _name = 'steps'
    _units = 'steps'


class StrokesField(Field):
    """Field that holds strokes measurement for sports activity."""

    _name = 'strokes'
    _units = 'strokes'
    _scale = 2.0


class SwimStrokesField(NamedField):
    """Field that holds strokes measurement for sports activity."""

    _name = 'swim_strokes'
    _units = 'strokes'


class CyclesDistanceField(Field):

    _name = 'cycles_to_distance'
    _units = 'm/cycle'
    _scale = 5000.0


class FractionalCyclesField(Field):
    """Field that holds cycles measurement for sports activity."""

    _name = 'total_fractional_cycles'
    _units = 'cycles'
    _scale = 128.0


class EventDataField(Field):
    """A field that holds data that depends on the event's type."""

    _name = 'event_data'
    _dependant_field = {
        'timer' : Field(name='timer_trigger'),
        245     : CyclesField
    }
    _dependant_field_control_fields = ['event']

    def dependant_field(self, control_value_list):
        """Return a field whose type is based on the event type."""
        event = control_value_list[0]
        return EventDataField._dependant_field[event]


class FractionalCadenceField(NamedField):

    _name = 'fractional_cadence'
    _units = 'rpm'
    _scale = 128.0


class PowerField(NamedField):
    """A field that holds a power measurement."""

    _name = 'power'
    _units = 'watts'


class TrainingEffectField(FloatField):
    """A field that holds a Garmin training effect measurement (0.0-5.0)."""

    _scale = 10.0
    _precision = 1


class TrainingLoadField(FloatField):
    """A field that holds a Garmin training load measurement."""

    _name = 'training_load'
    _scale = 65536.0
    _precision = 1


class ClimbingGradeField(NamedField):
    _name = 'grade'


class SportBasedGradeField(NamedField):
    """A climbing route grade field that generates dependant fields based on the sport and subsport type."""

    _dependant_field_control_fields = ['sport', 'sub_sport']
    _subsport_to_field = {
        SubSport.bouldering : BoulderingFontGradeField,
        SubSport.indoor_climbing : IndoorFontGradeField
    }

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        sport = control_value_list[0]
        if sport is Sport.rock_climbing:
            sub_sport = control_value_list[1]
            dependant_field = self._cycles_name_to_field.get(sub_sport, ClimbingGradeField)
        else:
            dependant_field = ClimbingGradeField
        return dependant_field()


class ClimbingRouteComletedField(NamedField):
    _name = 'route_completed'

    def _convert_single(self, value, invalid):
        if value != invalid:
            if value == 3:
                return True
            elif value == 2:
                return False
