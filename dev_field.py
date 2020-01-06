"""Objects that represent FIT file developer message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
from Fit.object_fields import ObjectField
import Fit.measurement as measurement


class DevField(Field):
    """Class that handles a developer fields."""

    def __init__(self, name, units, scale=None, offset=None, *args, **kwargs):
        """Return a DevField instance."""
        self._units = [units, units]
        if scale is not None:
            self._conversion_factor = [scale, scale]
        if offset is not None:
            self._conversion_constant = [offset, offset]
        super().__init__(name=name, *args, **kwargs)


class DevObjectField(ObjectField):
    """Field held in a measurement object."""

    def __init__(self, name, scale, offset, obj_func, output_func):
        """Return a new instance of DevSpeedField."""
        if scale is None:
            scale = 1.0
        if offset is None:
            offset = 1.0
        super().__init__(name, obj_func, output_func, scale, offset)


class DevDistanceField(DevObjectField):
    """Field holding a distance measurement."""

    units_to_obj_func = {
        'm'     : measurement.Distance.from_meters,
        'ft'     : measurement.Distance.from_feet,
        'km'    : measurement.Distance.from_kilometers,
        'mi'    : measurement.Distance.from_miles
    }

    def __init__(self, name, units, scale, offset, output_func=measurement.Distance.feet_or_meters):
        """Return a new instance of DevDistanceField."""
        super().__init__(name, scale, offset, self.units_to_obj_func[units], output_func)


class DerivedDevDistanceField(DevDistanceField):
    """Field holding a distance measurement."""

    def __init__(self, name, units, scale, offset, object_field):
        """Return a new instance of DerivedDevDistanceField."""
        super().__init__(name, units, scale, offset, object_field.output_func)


class DevSpeedField(DevObjectField):
    """Field holding a speed measurement."""

    units_to_obj_func = {
        'mps'   : measurement.Speed.from_mps,
        'km/h'  : measurement.Speed.from_kph,
        'kph'   : measurement.Speed.from_kph,
        'mph'   : measurement.Speed.from_mph
    }

    def __init__(self, name, units, scale, offset, output_func=measurement.Speed.mph_or_kph):
        """Return a new instance of DevSpeedField."""
        super().__init__(name, scale, offset, self.units_to_obj_func[units], output_func)


class DerivedDevSpeedField(DevSpeedField):
    """Field holding a speed measurement."""

    def __init__(self, name, units, scale, offset, object_field):
        """Return a new instance of DerivedDevSpeedField."""
        super().__init__(name, units, scale, offset, object_field.output_func)
