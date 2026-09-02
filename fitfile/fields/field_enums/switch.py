"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class Switch(Enum):
    """An enum representing a FIT switch field value."""

    off         = 0
    on          = 1
    auto        = 2
    invalid     = 255
