"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class FitBaseUnit(Enum):
    other       = 0
    kg          = 1
    lb          = 2
    invalid     = 255
