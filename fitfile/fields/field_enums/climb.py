"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class ClimbProEvent(Enum):
    """A enum that contains an event from a climbing program."""

    approach        = 0
    start           = 1
    complete        = 2
