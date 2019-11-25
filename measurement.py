"""Objects that represents measurements."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import Fit.field_enums as fe


class Measurement(object):
    """Object that represents measurement."""

    def __init__(self, raw_value, invalid_value, default_output_func=None, default_output_units=None):
        self.raw_value = raw_value
        self.invalid_value = invalid_value
        self.default_output_func = default_output_func
        self.default_output_units = default_output_units

    def is_invalid(self):
        """Return if the measurement is valid."""
        return (self.raw_value == self.invalid_value)

    def __repr__(self):
        """Return a string representation of a Measurement instance."""
        if self.is_invalid():
            value = 'invalid'
        else:
            value = '%s %s [%s]' % (self.default_output_func(), self.default_output_units, self.raw_value)
        return self.__class__.__name__ + '(' + value + ')'

    def __str__(self):
        """Return a string representation of a Measurement instance."""
        return self.__repr__()


class Distance(Measurement):
    """An object that handles convertions of distance mesaurements from one representation to another."""

    def __init__(self, meters, raw_value, invalid_value):
        """Return an instance of ther Distance class."""
        super(Distance, self).__init__(raw_value, invalid_value, self.to_meters, 'meters')
        self.meters = meters

    @classmethod
    def from_meters(cls, meters, invalid_value=None):
        """Create a Distance object from a distance measurement in meters."""
        return cls(meters, meters, invalid_value)

    @classmethod
    def from_cm(cls, cm, invalid_value=None):
        """Create a Distance object from a distance measurement in centimeters."""
        if cm is not None:
            return cls(cm / 100.0, cm, invalid_value)
        return cls(None, cm, invalid_value)

    @classmethod
    def from_mm(cls, mm, invalid_value=None):
        """Create a Distance object from a distance measurement in millimeters."""
        if mm is not None:
            return cls(mm / 1000.0, mm, invalid_value)
        return cls(None, mm, invalid_value)

    @classmethod
    def from_feet(cls, feet, invalid_value=None):
        """Create a Distance object from a distance measurement in feet."""
        if feet is not None:
            return cls(feet / 3.2808399, feet, invalid_value)
        return cls(None, feet, invalid_value)

    @classmethod
    def from_meters_or_feet(cls, distance, measurement_system=fe.DisplayMeasure.metric):
        """Return a distance object."""
        return cls.from_meters(distance) if measurement_system is fe.DisplayMeasure.metric else cls.from_feet(distance)

    def to_mm(self):
        if self.meters is not None:
            return self.meters * 1000.0

    def to_meters(self):
        if self.meters is not None:
            return self.meters

    def to_kms(self):
        if self.meters is not None:
            return (self.meters / 1000.0)

    def to_inches(self):
        if self.meters is not None:
            return (self.meters * 39.37008)

    def to_feet(self):
        if self.meters is not None:
            return (self.meters * 3.2808399)

    def to_miles(self):
        if self.meters is not None:
            return (self.meters * 0.0006213712)

    @classmethod
    def mm_or_inches(cls, distance, measurement_system=fe.DisplayMeasure.metric):
        return distance.mm_or_inches(measurement_system)

    def mm_or_inches(self, measurement_system=fe.DisplayMeasure.metric):
        if self.meters is not None:
            return self.to_mm() if measurement_system is fe.DisplayMeasure.metric else self.to_inches()

    @classmethod
    def meters_or_feet(cls, distance, measurement_system=fe.DisplayMeasure.metric):
        return distance.meters_or_feet(measurement_system)

    def meters_or_feet(self, measurement_system=fe.DisplayMeasure.metric):
        if self.meters is not None:
            return self.to_meters() if measurement_system is fe.DisplayMeasure.metric else self.to_feet()

    @classmethod
    def kms_or_miles(cls, distance, measurement_system=fe.DisplayMeasure.metric):
        return distance.kms_or_miles(measurement_system)

    def kms_or_miles(self, measurement_system=fe.DisplayMeasure.metric):
        if self.meters is not None:
            return self.to_kms() if measurement_system is fe.DisplayMeasure.metric else self.to_miles()


class Position(Measurement):
    """Object that represents position measurement."""

    def __init__(self, semicircles, raw_value, invalid_value):
        super(Position, self).__init__(raw_value, invalid_value, self.to_degrees, 'degrees')
        self.semicircles = semicircles

    @classmethod
    def from_semicircles(cls, semicircles, invalid_value=None):
        return cls(semicircles, semicircles, invalid_value)

    @classmethod
    def to_degrees(cls, position, measurement_system=fe.DisplayMeasure.metric):
        return position.to_degrees(measurement_system)

    def to_degrees(self, measurement_system=fe.DisplayMeasure.metric):
        return (self.semicircles  / 11930326.891)


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
        super(Speed, self).__init__(raw_value, invalid_value, self.to_mph, 'mph')
        self.meters_per_sec = meters_per_sec

    @classmethod
    def from_mps(cls, meters_per_sec, invalid_value=None):
        """Return a Speed instance intialized with a value in meters per sec."""
        return cls(meters_per_sec, meters_per_sec, invalid_value)

    @classmethod
    def from_kph(cls, km_per_hour, invalid_value=None):
        """Return a Speed instance intialized with a value in kilometers per hour."""
        if km_per_hour is not None:
            return cls(km_per_hour * 1000.0, km_per_hour, invalid_value)
        return cls(None, km_per_hour, invalid_value)

    @classmethod
    def from_mph(cls, miles_per_hour, invalid_value=None):
        """Return a Speed instance intialized with a value in miles per hour."""
        if miles_per_hour is not None:
            return cls(miles_per_hour * 0.44704, miles_per_hour, invalid_value)
        return cls(None, miles_per_hour, invalid_value)

    @classmethod
    def from_cps(cls, centimeters_per_sec, invalid_value=None):
        """Return a Speed instance intialized with a value in centimeters per sec."""
        if centimeters_per_sec is not None:
            return cls(centimeters_per_sec / 100.0, centimeters_per_sec, invalid_value)
        return cls(None, centimeters_per_sec, invalid_value)

    @classmethod
    def from_mmps(cls, mm_per_sec, invalid_value=None):
        """Return a Speed instance intialized with a value in millimeters per sec."""
        if mm_per_sec is not None:
            return cls(mm_per_sec / 1000.0, mm_per_sec, invalid_value)
        return cls(None, mm_per_sec, invalid_value)

    @classmethod
    def from_kph_or_mph(cls, speed, measurement_system=fe.DisplayMeasure.metric):
        return cls.from_kph(speed) if measurement_system is fe.DisplayMeasure.metric else cls.from_mph(speed)

    def to_kph(self):
        if self.meters_per_sec is not None:
            return ((self.meters_per_sec * (60 * 60)) / 1000.0)

    def to_mph(self):
        if self.meters_per_sec is not None:
            return (self.meters_per_sec * 2.236936)

    def to_mps(self):
        return self.meters_per_sec

    @classmethod
    def kph_or_mph(cls, speed, measurement_system=fe.DisplayMeasure.metric):
        return speed.kph_or_mph(measurement_system)

    def kph_or_mph(self, measurement_system=fe.DisplayMeasure.metric):
        if self.meters_per_sec is not None:
            return self.to_kph() if measurement_system is fe.DisplayMeasure.metric else self.to_mph()


class Weight(Measurement):
    def __init__(self, kgs, raw_value, invalid_value):
        super(Weight, self).__init__(raw_value, invalid_value, self.to_lbs, 'lbs')
        self.kgs = kgs

    @classmethod
    def from_grams(cls, grams, invalid_value=None):
        return cls(grams / 1000.0, grams, invalid_value)

    @classmethod
    def from_cgs(cls, centigrams, invalid_value=None):
        return cls(centigrams / 10.0, centigrams, invalid_value)

    @classmethod
    def from_lbs(cls, lbs, invalid_value=None):
        return cls(lbs / 2.204623, lbs, invalid_value)

    def to_kgs(self):
        return self.kgs

    def to_lbs(self):
        return (self.kgs * 2.204623)

    @classmethod
    def kgs_or_lbs(cls, weight, measurement_system=fe.DisplayMeasure.metric):
        return weight.kgs_or_lbs(measurement_system)

    def kgs_or_lbs(self, measurement_system=fe.DisplayMeasure.metric):
        if self.kgs is not None:
            return self.to_kgs() if measurement_system is fe.DisplayMeasure.metric else self.to_lbs()


class Temperature(Measurement):
    def __init__(self, celsius, raw_value, invalid_value):
        super(Temperature, self).__init__(raw_value, invalid_value, self.to_f, 'F')
        self.celsius = celsius

    @classmethod
    def from_celsius(cls, celsius, invalid_value=None):
        return cls(celsius, celsius, invalid_value)

    def to_f(self):
        return (self.celsius * 1.8) + 32.0

    @classmethod
    def c_or_f(cls, temperature, measurement_system=fe.DisplayMeasure.metric):
        return temperature.c_or_f(measurement_system)

    def c_or_f(self, measurement_system=fe.DisplayMeasure.metric):
        if self.celsius is not None:
            return self.celsius if measurement_system is fe.DisplayMeasure.metric else self.to_f()
