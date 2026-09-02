"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class GoalType(Enum):
    time            = 0
    distance        = 1
    calories        = 2
    frequency       = 3
    steps           = 4
    ascent          = 5
    active_minutes  = 6


class GoalSource(Enum):
    auto            = 0
    community       = 1
    user            = 2


class GoalRecurrence(Enum):
    off             = 0
    daily           = 1
    weekly          = 2
    monthly         = 3
    yearly          = 4
    custom          = 5


class PersonalRecordType(Enum):
    time        = 0
    distance    = 1
    elevation   = 2
    power       = 3
