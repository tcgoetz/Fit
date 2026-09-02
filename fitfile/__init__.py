"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa


from .version_info import version_string, __version__

from .enum import UnknownEnumValue, name_for_enum
from .file import File
from .message_type import MessageType, UnknownMessageType
from .measurement import MeasurementSystem, Distance, Latitude, Longitude, Speed, Weight, Volume, Temperature, Cadence
from .units import unit_strings

#
# field_enums
#
from .fields import Switch, GarminProduct, Manufacturer, BatteryStatus, FileType
