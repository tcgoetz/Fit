"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import file
import exceptions
from message_type import UnknownMessageType, MessageType
import field_enums
import conversions
import units
from measurement import Distance, Latitude, Longitude, Speed, Weight, Temperature
