#
# copyright Tom Goetz
#

from Metric import Metric
from FieldEnums import DisplayMeasure


class Position(Metric):
    def __init__(self, semicircles, raw_value, invalid_value):
        super(Position, self).__init__(raw_value, invalid_value, self.to_degrees, 'degrees')
        self.semicircles = semicircles

    @classmethod
    def from_semicircles(cls, semicircles, invalid_value=None):
        return cls(semicircles, semicircles, invalid_value)

    @classmethod
    def to_degrees(cls, position, measurement_system=DisplayMeasure.metric):
        return position.to_degrees(measurement_system)

    def to_degrees(self, measurement_system=DisplayMeasure.metric):
        return (self.semicircles  / 11930326.891)


class Latitude(Position):
    pass


class Longitude(Position):
    pass
