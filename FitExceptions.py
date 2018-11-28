#!/usr/bin/env python

#
# copyright Tom Goetz
#

import traceback


class FitException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class FitFileError(FitException):
    pass


class FitFileBadHeaderSize(FitFileError):
    pass


class FitFileBadProtocolVersion(FitFileError):
    pass


class FitFileDataType(FitFileError):
    pass


class FitMessageType(FitFileError):
    pass


class FitUndefDevMessageType(FitFileError):
    pass


class FitDependantField(FitFileError):
    pass
