"""Objects that represent exceptions while parsing a FIT file."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


class FitException(Exception):
    """Base class for FIT file exceptions."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class FitFileError(FitException):
    pass


class FitFileBadHeaderSize(FitFileError):
    """An exception do to a bad FIT file header size."""

    pass


class FitFileBadProtocolVersion(FitFileError):
    """An exception do to a bad FIT file protocol version."""

    pass


class FitFileDataType(FitFileError):
    pass


class FitMessageType(FitFileError):
    """An exception do to a unrecognized FIT file message type."""

    pass


class FitMessageParse(FitFileError):
    pass


class FitUndefDevMessageType(FitFileError):
    pass


class FitDependantField(FitFileError):
    pass


class FitOutOfOrderMessage(FitFileError):
    pass
