"""Units strings for measurement systems."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import enum

from .field_enums import DisplayMeasure


class UnitTypes(enum.Enum):
    """An enumeration of unit types."""

    distance_long   = 1
    pace            = 2
    speed           = 3


unit_strings = {
    DisplayMeasure.statute : {
        UnitTypes.distance_long : 'miles',
        UnitTypes.pace          : 'per mile',
        UnitTypes.speed         : 'mph'
    },
    DisplayMeasure.metric : {
        UnitTypes.distance_long : 'kilometers',
        UnitTypes.pace          : 'per kilometers',
        UnitTypes.speed         : 'kph'
    }
}
