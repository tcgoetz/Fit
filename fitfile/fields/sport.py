"""Objects that represent FIT file sport message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .field import Field, NamedField


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


class TrainingEffectField(NamedField):
    """A field that holds a Garmin training effect measurement (0.0-5.0)."""

    _scale = 10.0


#
# Climbing related fields
#
class ClimbingGrade(NamedField):
    _name = 'grade'


class ClimbingRouteComleted(NamedField):
    _name = 'route_completed'

    def _convert_single(self, value, invalid):
        if value != invalid:
            if value == 3:
                return True
            elif value == 2:
                return False
