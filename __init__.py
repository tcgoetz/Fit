"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa

from Fit.file import File
import Fit.exceptions
from Fit.message_type import UnknownMessageType, MessageType
import Fit.field_enums as field_enums
from Fit.file_type import FileType
from Fit.manufacturer import Manufacturer
from Fit.product import GarminProduct, GarminLocalProduct, ScoscheProduct, WahooFitnessProduct, UnknownProduct, product_enum
from Fit.sport import Sport, SubSport
from Fit.device_enums import MainDeviceType, AntplusDeviceType, LocalDeviceType, UnknownDeviceType
import Fit.conversions as conversions
import Fit.units as units
from Fit.measurement import Distance, Latitude, Longitude, Speed, Weight, Volume, Temperature, Cadence
