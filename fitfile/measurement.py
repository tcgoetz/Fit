"""Objects that represents measurements."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import logging

from .field_enums import DisplayMeasure


logger = logging.getLogger(__name__)


class Measurement():
    """Object that represents measurement."""

    def __init__(self, value, raw_value, invalid_value, default_output_func=None, default_output_units=None):
        """Return a Measurement instance."""
        self.value = value
        self.raw_value = raw_value
        self.invalid_value = invalid_value
        self.default_output_func = default_output_func
        self.default_output_units = default_output_units

    @classmethod
    def from_units(cls, value, scale, invalid_value=None):
        """Create a Distance object from a distance measurement."""
        return cls((value * scale) if value is not None else None, value, invalid_value)

    def to_units(self, scale=1.0, rounded=False):
        """Return a measurement value given the current value and a scale."""
        if not self.is_invalid():
            try:
                value = self.value * scale
                return round(value) if rounded else value
            except Exception as e:
                raise Exception(f'value {self.value} scale {scale}: {e}')

    def is_invalid(self):
        """Return if the measurement is valid."""
        return (self.raw_value is None) or (self.raw_value == self.invalid_value)

    def __eq__(self, other):
        if not isinstance(other, Measurement):
            return NotImplemented
        return (self.value == other.value)

    def __repr__(self):
        """Return a string representation of a Measurement instance."""
        if self.is_invalid():
            value = 'invalid'
        else:
            value = f'{self.default_output_func()} {self.default_output_units} [{self.raw_value}, {self.invalid_value}]'
        return f'{self.__class__.__name__ }({value})'

    def __str__(self):
        """Return a string representation of a Measurement instance."""
        return self.__repr__()


class Distance(Measurement):
    """An object that handles convertions of distance mesaurements from one representation to another."""

    def __init__(self, meters, raw_value, invalid_value):
        """Return an instance of the Distance class."""
        super().__init__(meters, raw_value, invalid_value, self.to_meters, 'meters')

    @classmethod
    def from_kilometers(cls, kms, invalid_value=None):
        """Create a Distance object from a distance measurement in kilometers."""
        return cls.from_units(kms, 1000.0, invalid_value)

    @classmethod
    def from_meters(cls, meters, invalid_value=None):
        """Create a Distance object from a distance measurement in meters."""
        return cls(meters, meters, invalid_value)

    @classmethod
    def from_cm(cls, cm, invalid_value=None):
        """Create a Distance object from a distance measurement in centimeters."""
        return cls.from_units(cm, 0.01, invalid_value)

    @classmethod
    def from_mm(cls, mm, invalid_value=None):
        """Create a Distance object from a distance measurement in millimeters."""
        return cls.from_units(mm, 0.001, invalid_value)

    @classmethod
    def from_feet(cls, feet, invalid_value=None):
        """Create a Distance object from a distance measurement in feet."""
        return cls.from_units(feet, 0.3048, invalid_value)

    @classmethod
    def from_miles(cls, feet, invalid_value=None):
        """Create a Distance object from a distance measurement in miles."""
        return cls.from_units(feet, 1609.344, invalid_value)

    @classmethod
    def from_unknown(cls, value, invalid_value=None):
        """Create a Distance object from a distance measurement with unknown units."""
        return cls.from_units(value, 1.0, invalid_value)

    @classmethod
    def from_func(cls, units):
        """Return a Distance object from function for a measurement in units."""
        units_to_obj_func = {
            'cm': cls.from_cm,
            'centimeters': cls.from_cm,
            'm': cls.from_meters,
            'meters': cls.from_meters,
            'km': cls.from_kilometers,
            'kilometers': cls.from_kilometers,
            'ft': cls.from_feet,
            'feet': cls.from_feet,
            'mi': cls.from_miles,
            'miles': cls.from_miles
        }
        try:
            return units_to_obj_func[units.lower()]
        except KeyError:
            logger.error(f'No conversion for distance units {units}')
            return cls.from_unknown

    @classmethod
    def from_meters_or_feet(cls, distance, measurement_system=DisplayMeasure.metric):
        """Return a distance object."""
        return cls.from_meters(distance) if measurement_system is DisplayMeasure.metric else cls.from_feet(distance)

    def to_mm(self):
        """Return the distance measurement as millimeters."""
        return self.to_units(1000.0)

    def to_meters(self):
        """Return the distance measurement as meters."""
        return self.to_units()

    def to_kms(self):
        """Return the distance measurement as kilometers."""
        return self.to_units(0.001)

    def to_inches(self):
        """Return the distance measurement as inches."""
        return self.to_units(39.37008)

    def to_feet(self):
        """Return the distance measurement as feet."""
        return self.to_units(3.2808399)

    def to_miles(self):
        """Return the distance measurement as miles."""
        return self.to_units(0.0006213712)

    @classmethod
    def inches_or_mm(cls, distance, measurement_system=DisplayMeasure.metric):
        """Return the distance measurement as millimeters or inches depending on the measurement system."""
        return distance.mm_or_inches(measurement_system)

    def mm_or_inches(self, measurement_system=DisplayMeasure.metric):
        """Return the distance measurement as millimeters or inches depending on the measurement system."""
        return self.to_mm() if measurement_system is DisplayMeasure.metric else self.to_inches()

    @classmethod
    def feet_or_meters(cls, distance, measurement_system=DisplayMeasure.metric):
        """Return the distance measurement as meters or feet depending on the measurement system."""
        return distance.meters_or_feet(measurement_system)

    def meters_or_feet(self, measurement_system=DisplayMeasure.metric):
        """Return the distance measurement as meters or feet depending on the measurement system."""
        return self.to_meters() if measurement_system is DisplayMeasure.metric else self.to_feet()

    #
    # @classmethod
    # def kms_or_miles(cls, distance, measurement_system=DisplayMeasure.metric):
    #     """Return the distance measurement as kilometers or miles depending on the measurement system."""
    #     return distance.kms_or_miles(measurement_system)

    def kms_or_miles(self, measurement_system=DisplayMeasure.metric):
        """Return the distance measurement as kilometers or miles depending on the measurement system."""
        return self.to_kms() if measurement_system is DisplayMeasure.metric else self.to_miles()


class Position(Measurement):
    """Object that represents position measurement."""

    def __init__(self, semicircles, raw_value, invalid_value):
        """Return an instance of the Position class."""
        super().__init__(semicircles, raw_value, invalid_value, self.to_degrees, 'degrees')

    @classmethod
    def from_semicircles(cls, semicircles, invalid_value=None):
        """Return a Position instance intialized from a value measured in semicircles."""
        return cls(semicircles, semicircles, invalid_value)

    # @classmethod
    # def to_degrees(cls, position, measurement_system=DisplayMeasure.metric):
    #     return position.to_degrees(measurement_system)

    def to_degrees(self, measurement_system=DisplayMeasure.metric):
        """Return the position measurement as degrees."""
        return self.to_units(180.0 / 2147483648.0)


class Latitude(Position):
    """Object that represents position latitude."""

    pass


class Longitude(Position):
    """Object that represents position longitude."""

    pass


class Speed(Measurement):
    """Object that represents a speed measurement."""

    def __init__(self, meters_per_sec, raw_value, invalid_value):
        """Return a Speed instance intialized with a value in meters per sec."""
        super().__init__(meters_per_sec, raw_value, invalid_value, self.to_mph, 'mph')

    @classmethod
    def from_mps(cls, meters_per_sec, invalid_value=None):
        """Return a Speed instance intialized with a value in meters per sec."""
        return cls(meters_per_sec, meters_per_sec, invalid_value)

    @classmethod
    def from_kph(cls, km_per_hour, invalid_value=None):
        """Return a Speed instance intialized with a value in kilometers per hour."""
        return cls.from_units(km_per_hour, 0.2777778, invalid_value)

    @classmethod
    def from_mph(cls, miles_per_hour, invalid_value=None):
        """Return a Speed instance intialized with a value in miles per hour."""
        return cls.from_units(miles_per_hour, 0.44704, invalid_value)

    @classmethod
    def from_cps(cls, centimeters_per_sec, invalid_value=None):
        """Return a Speed instance intialized with a value in centimeters per sec."""
        return cls.from_units(centimeters_per_sec, 0.01, invalid_value)

    @classmethod
    def from_mmps(cls, mm_per_sec, invalid_value=None):
        """Return a Speed instance intialized with a value in millimeters per sec."""
        return cls.from_units(mm_per_sec, 0.001, invalid_value)

    @classmethod
    def from_unknown(cls, value, invalid_value=None):
        """Create a Speed object from a speed value with unknown units."""
        return cls.from_units(value, 1.0, invalid_value)

    @classmethod
    def from_func(cls, units):
        """Return a Distance object from function for a measurement in units."""
        units_to_obj_func = {
            'mps'   : cls.from_mps,
            'm/s'   : cls.from_mps,
            'kph'   : cls.from_kph,
            'km/h'  : cls.from_kph,
            'mph'   : cls.from_mph,
            'm/h'   : cls.from_mph
        }
        try:
            return units_to_obj_func[units.lower()]
        except KeyError:
            logger.error(f'No conversion for speed units {units}')
            return cls.from_unknown

    @classmethod
    def from_kph_or_mph(cls, speed, measurement_system=DisplayMeasure.metric):
        """Return a Speed instance intialized with a value in kilometers per hopur or miles per hour."""
        return cls.from_kph(speed) if measurement_system is DisplayMeasure.metric else cls.from_mph(speed)

    def to_kph(self):
        """Return the speed measurement as kilometers per hour."""
        return self.to_units(3.6)

    def to_mph(self):
        """Return the speed measurement as miles per hour."""
        return self.to_units(2.236936)

    def to_mps(self):
        """Return the speed measurement as meters per second."""
        return self.value

    @classmethod
    def mph_or_kph(cls, speed, measurement_system=DisplayMeasure.metric):
        """Return the speed measurement as kilometers per hour or miles per hour."""
        return speed.kph_or_mph(measurement_system)

    def kph_or_mph(self, measurement_system=DisplayMeasure.metric):
        """Return the speed measurement as kilometers per hour or miles per hour."""
        return self.to_kph() if measurement_system is DisplayMeasure.metric else self.to_mph()


class Weight(Measurement):
    """Object that represents a weight measurement."""

    def __init__(self, kgs, raw_value, invalid_value):
        """Return a Weight instance intialized with a value in kilograms."""
        super().__init__(kgs, raw_value, invalid_value, self.to_lbs, 'lbs')

    @classmethod
    def from_grams(cls, grams, invalid_value=None):
        """Return a Weight instance created from a value in grams."""
        return cls.from_units(grams, 0.001, invalid_value)

    @classmethod
    def from_cgs(cls, centigrams, invalid_value=None):
        """Return a Weight instance created from a value in centigrams."""
        return cls.from_units(centigrams, 0.1, invalid_value)

    @classmethod
    def from_lbs(cls, lbs, invalid_value=None):
        """Return a Weight instance created from a value in pounds."""
        return cls.from_units(lbs, 0.4535924, invalid_value)

    def to_kgs(self):
        """Return the weight measurement as kilograms."""
        return self.value

    def to_lbs(self):
        """Return the weight measurement as pounds."""
        return self.to_units(2.204623)

    @classmethod
    def lbs_or_kgs(cls, weight, measurement_system=DisplayMeasure.metric):
        """Return the weight measurement as kilograms or pounds."""
        return weight.kgs_or_lbs(measurement_system)

    def kgs_or_lbs(self, measurement_system=DisplayMeasure.metric):
        """Return the weight measurement as kilograms or pounds."""
        return self.to_kgs() if measurement_system is DisplayMeasure.metric else self.to_lbs()


class Volume(Measurement):
    """Object that represents a volume measurement."""

    def __init__(self, kgs, raw_value, invalid_value):
        """Return a Volume instance intialized with a value in liters."""
        super().__init__(kgs, raw_value, invalid_value, self.to_ounces, 'Ounces')

    @classmethod
    def from_milliliters(cls, milliliters, invalid_value=None):
        """Return a Volume instance created from a value in milliliters."""
        return cls.from_units(milliliters, 0.001, invalid_value)

    def to_liters(self):
        """Return the volume measurement as liters."""
        return self.value

    def to_milliliters(self, rounded=False):
        """Return the volume measurement as milliliters."""
        return self.to_units(1000.0, rounded=rounded)

    def to_ounces(self, rounded=False):
        """Return the volume measurement as ounces."""
        return self.to_units(35.19503, rounded=rounded)

    def ml_or_oz(self, measurement_system=DisplayMeasure.metric, rounded=False):
        """Return the volume measurement as milliliters or ounces."""
        return self.to_milliliters(rounded) if measurement_system is DisplayMeasure.metric else self.to_ounces(rounded)


class Temperature(Measurement):
    """Object that represents a temperature measurement."""

    def __init__(self, celsius, raw_value, invalid_value):
        """Return a Temperature instance intialized with a value in celsius."""
        super().__init__(celsius, raw_value, invalid_value, self.to_f, 'F')

    @classmethod
    def from_celsius(cls, celsius, invalid_value=None):
        """Return a Temperature instance intialized with a value in celsius."""
        return cls(celsius, celsius, invalid_value)

    def to_f(self):
        """Return the temperature measurement as farenheit."""
        if self.value is not None:
            return (self.value * 1.8) + 32.0

    @classmethod
    def f_or_c(cls, temperature, measurement_system=DisplayMeasure.metric):
        """Return the temperature measurement as farenheit or celsius."""
        return temperature.c_or_f(measurement_system)

    def c_or_f(self, measurement_system=DisplayMeasure.metric):
        """Return the temperature measurement as farenheit or celsius."""
        return self.value if measurement_system is DisplayMeasure.metric else self.to_f()


class Cadence(Measurement):
    """Object that represents a cadence measurement."""

    def __init__(self, cycles, raw_value, invalid_value):
        """Return a Cadence instance intialized with a value in cycles."""
        super().__init__(cycles, raw_value, invalid_value, self.to_cycles, 'cycles')

    @classmethod
    def from_cycles(cls, cycles, invalid_value=None):
        """Return a Temperature instance intialized with a value in celsius."""
        return cls(cycles, cycles, invalid_value)

    def to_cycles(self):
        """Return the cadence measurement as cycles."""
        return self.value

    def to_spm(self):
        """Return the cadence measurement as steps per minute."""
        if self.value is not None:
            return (self.value * 2)
