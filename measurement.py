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
        super(Distance, self).__init__(raw_value, invalid_value, self.to_meters, 'meters')
        self.meters = meters

    @classmethod
    def from_meters(cls, meters, invalid_value=None):
        """Create a Distance object from a distance measurement in meters."""
        return cls(meters, meters, invalid_value)

    @classmethod
    def from_cm(cls, cm, invalid_value=None):
        """Create a Distance object from a distance measurement in centimeters."""
        return cls(cm / 100.0, cm, invalid_value)

    @classmethod
    def from_mm(cls, mm, invalid_value=None):
        """Create a Distance object from a distance measurement in millimeters."""
        return cls(mm / 1000.0, mm, invalid_value)

    @classmethod
    def from_feet(cls, feet, invalid_value=None):
        """Create a Distance object from a distance measurement in feet."""
        return cls(feet / 3.2808399, feet, invalid_value)

    def to_mm(self):
        return self.meters * 1000.0

    def to_meters(self):
        return self.meters

    def to_kms(self):
        return (self.meters / 1000.0)

    def to_inches(self):
        return (self.meters * 39.37008)

    def to_feet(self):
        return (self.meters * 3.2808399)

    def to_miles(self):
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
        super(Speed, self).__init__(raw_value, invalid_value, self.to_mph, 'mph')
        self.meters_per_sec = meters_per_sec

    @classmethod
    def from_mps(cls, meters_per_sec, invalid_value=None):
        return cls(meters_per_sec, meters_per_sec, invalid_value)

    @classmethod
    def from_cps(cls, centimeters_per_sec, invalid_value=None):
        return cls(centimeters_per_sec / 100.0, centimeters_per_sec, invalid_value)

    @classmethod
    def from_mmps(cls, mm_per_sec, invalid_value=None):
        return cls(mm_per_sec / 1000.0, mm_per_sec, invalid_value)

    def to_kph(self):
        return ((self.meters_per_sec * (60 * 60)) / 1000.0)

    def to_mph(self):
        return (self.meters_per_sec * 2.236936)

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
