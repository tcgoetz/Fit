"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa

from .file import File
from .message_type import UnknownMessageType, MessageType
from .file_type import FileType
from .manufacturer import Manufacturer
from .product import GarminProduct, GarminLocalProduct, ScoscheProduct, WahooFitnessProduct, UnknownProduct, product_enum
from .sport import Sport, SubSport
from .device_enums import MainDeviceType, AntplusDeviceType, LocalDeviceType, UnknownDeviceType
from .units import UnitTypes, unit_strings
from .measurement import Distance, Latitude, Longitude, Speed, Weight, Volume, Temperature, Cadence
from .version_info import version_string, __version__
