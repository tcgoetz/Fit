"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class AlertMetric(Enum):
    time        = 0
    distance    = 1
    calories    = 2
    ascent      = 3
    descent     = 4
    reps        = 5
    smart       = 7
    pacing      = 8
