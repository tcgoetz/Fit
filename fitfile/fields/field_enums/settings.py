"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class VolumeUnits(Enum):
    """Enum of values used to encode volume units."""

    ounces = 1
    milliliters = 2


class SelfEvaluationStatus(Enum):
    """Enum of values used to encode ."""

    off = 0
    workouts_only = 1
    always = 2


class TouchStatus(Enum):
    """Enum of values used to encode ."""

    off = 0
    on = 1
    system = 2
    map_only = 3


class RunningPowerMode(Enum):
    """Enum of values used to encode ."""

    off = 0
    accessory_mode = 1
    wrist_only = 2
    smart_mode = 3


class ClimbProMode(Enum):
    """Enum of values used to encode ."""

    when_navigating = 1
    always = 2


class ClimbDetection(Enum):
    """Enum of values used to encode ."""

    cat_4 = 1
    cat_3 = 2
    cat_2 = 3
    cat_1 = 4
    hc = 5
    uncategorized = 6


class ClimbProTerrain(Enum):
    """Enum of values used to encode ."""

    paved = 1
    unpaved = 2
    mixed = 3


class TapSensitivity(Enum):
    """Enum of values used to encode ."""

    high = 0
    medium = 1
    low = 2


class AutoScrollMode(Enum):
    off = 0
    slow = 1
    medium = 2
    fast = 3


class AutoPauseSetting(Enum):
    off = 0
    when_stopped = 1
    custom = 2
