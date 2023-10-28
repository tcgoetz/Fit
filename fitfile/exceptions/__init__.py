"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa

from .exceptions import FitException, FitFileError, FitFileBadHeaderSize, FitFileBadProtocolVersion, FitFileDataType, FitMessageType, FitMessageParse, FitDataFieldParse, FitUndefDevMessageType, FitOutOfOrderMessage
