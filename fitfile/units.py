"""Units strings for measurement systems."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import enum

from .measurement import MeasurementSystem


class UnitTypes(enum.Enum):
    """An enumeration of unit types."""

    distance_long   = 1
    pace            = 2
    speed           = 3
    altitude        = 4
    tempurature     = 5


unit_strings = {
    MeasurementSystem.statute : {
        UnitTypes.distance_long : 'miles',
        UnitTypes.pace          : 'per mile',
        UnitTypes.speed         : 'mph',
        UnitTypes.altitude      : 'feet',
        UnitTypes.tempurature   : 'F'
    },
    MeasurementSystem.metric : {
        UnitTypes.distance_long : 'kilometers',
        UnitTypes.pace          : 'per kilometers',
        UnitTypes.speed         : 'kph',
        UnitTypes.altitude      : 'meters',
        UnitTypes.tempurature   : 'C'
    }
}
