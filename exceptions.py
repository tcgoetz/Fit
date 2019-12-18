"""Objects that represent exceptions while parsing a FIT file."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


class FitException(Exception):
    """Base class for FIT file exceptions."""

    def __init__(self, message):
        """Return a FitException instance."""
        self.message = message

    def __str__(self):
        """Return a string representation of a FitException instance."""
        return self.message


class FitFileError(FitException):
    """An exception when parsing a FIT file."""


class FitFileBadHeaderSize(FitFileError):
    """An exception do to a bad FIT file header size."""


class FitFileBadProtocolVersion(FitFileError):
    """An exception do to a bad FIT file protocol version."""


class FitFileDataType(FitFileError):
    """An exception happenbed will parsing FIT file data."""


class FitMessageType(FitFileError):
    """An exception do to a unrecognized FIT file message type."""


class FitMessageParse(FitFileError):
    """An exception happenbed will parsing a FIT file message."""


class FitUndefDevMessageType(FitFileError):
    """An undefined message type was encountered."""


class FitOutOfOrderMessage(FitFileError):
    """The message's timestamp preceeded the previous message's."""
