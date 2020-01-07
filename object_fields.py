"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
import Fit.field_enums as fe
from Fit.field_value import FieldValue
import Fit.measurement as measurement


class ObjectField(Field):
    """Class that handles a field that translates into a Python object."""

    def __init__(self, obj_func, output_func, **kwargs):
        self.obj_func = obj_func
        self.output_func = output_func
        super().__init__(**kwargs)

    def _invalid_single(self, value, invalid):
        return value.is_invalid()

    def _convert_single(self, value, invalid):
        return self.output_func(value, self.measurement_system)

    def convert(self, value, invalid, measurement_system=fe.DisplayMeasure.metric):
        """Returna FieldValue containing the field value as a Python object."""
        self.measurement_system = measurement_system
        value_obj = self.obj_func((value / self._scale) - self._offset, invalid)
        return FieldValue(self, invalid=invalid, value=self._convert_many(value_obj, invalid), orig=value_obj)

    def reconvert(self, value, invalid, measurement_system=fe.DisplayMeasure.metric):
        """Return a FieldValue containing the field value as a Python object."""
        self.measurement_system = measurement_system
        value_obj = self.obj_func((value / self._scale) - self._offset, invalid)
        return (self._convert_many(value_obj, invalid), value_obj)


class HeightField(ObjectField):
    """Class that handles a user height measurement from a FIT message field."""

    _name = 'height'

    def __init__(self):
        """Return a HeightField instance."""
        super().__init__(measurement.Distance.from_cm, measurement.Distance.feet_or_meters)


class WeightField(ObjectField):
    """Class that handles a user weight measurement from a FIT message field."""

    def __init__(self, name):
        """Return a WeightField instance."""
        super().__init__(measurement.Weight.from_cgs, measurement.Weight.lbs_or_kgs, name=name)


class SpeedMpsField(ObjectField):
    """Field holding a distance measure in meters per second."""

    def __init__(self, name):
        """Return a SpeedMpsField instance."""
        super().__init__(measurement.Speed.from_mmps, measurement.Speed.mph_or_kph, name=name)


class LongitudeField(ObjectField):
    """Field that handles a longitude measure in semicircles."""

    def __init__(self, name):
        """Return a LongitudeField instance."""
        super().__init__(measurement.Longitude.from_semicircles, measurement.Longitude.to_degrees, name=name)


class LatiitudeField(ObjectField):
    """Field that handles a latitude measure in semicircles."""

    def __init__(self, name):
        """Return a LatiitudeField instance."""
        super().__init__(measurement.Latitude.from_semicircles, measurement.Latitude.to_degrees, name=name)


class TemperatureField(ObjectField):
    """Field holding a temperature measurement in celsius."""

    def __init__(self, name):
        """Return a ObjectField instance."""
        super().__init__(measurement.Temperature.from_celsius, measurement.Temperature.f_or_c, name=name)


class DistanceMetersField(ObjectField):
    """Field holding a distance measurement in meters."""

    def __init__(self, name, obj_func=measurement.Distance.from_meters, output_func=measurement.Distance.feet_or_meters, **kwargs):
        """Return a new instance of DistanceMetersField."""
        super().__init__(obj_func, output_func, name=name, **kwargs)


class EnhancedDistanceMetersField(DistanceMetersField):
    """Field holding a distance measure in meters."""

    def __init__(self, name):
        """Return a EnhancedDistanceMetersField instance."""
        super().__init__(name, measurement.Distance.from_mm, measurement.Distance.feet_or_meters)


class DistanceCentimetersToKmsField(DistanceMetersField):
    """Field holding a distance measure in meters."""

    def __init__(self, name):
        """Return a DistanceCentimetersToKmsField instance."""
        super().__init__(name, measurement.Distance.from_cm, measurement.Distance.kms_or_miles)


class DistanceCentimetersToMetersField(DistanceMetersField):
    """Field holding a distance measure in meters."""

    def __init__(self, name):
        """Return a DistanceCentimetersToMetersField instance."""
        super().__init__(name, measurement.Distance.from_cm, measurement.Distance.feet_or_meters)


class DistanceMillimetersToMetersField(DistanceMetersField):
    """Field holding a distance measure in meters."""

    def __init__(self, name):
        """Return a DistanceMillimetersToMetersField instance."""
        super().__init__(name, measurement.Distance.from_mm, measurement.Distance.feet_or_meters)


class DistanceMillimetersField(DistanceMetersField):
    """Field holding a distance measure in meters."""

    def __init__(self, name):
        """Return a DistanceMillimetersField instance."""
        super().__init__(name, measurement.Distance.from_mm, measurement.Distance.inches_or_mm, scale=10.0)


class AltitudeField(DistanceMetersField):
    """A field containing a altitude reading."""

    def __init__(self):
        """Return an instance of AltitudeField."""
        super().__init__('altitude', measurement.Distance.from_cm, measurement.Distance.feet_or_meters, scale=5.0)


class EnhancedAltitudeField(DistanceMetersField):
    """A field containing a altitude reading with greater range."""

    _name = 'enhanced_altitude'

    def __init__(self, name):
        """Return an instance of EnhancedAltitudeField."""
        super().__init__(name, measurement.Distance.from_meters, measurement.Distance.feet_or_meters, scale=5.0, offset=500.0)
