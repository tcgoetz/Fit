"""Class that represents a FIT file header."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import collections

from .exceptions.exceptions import FitFileBadHeaderSize, FitFileBadProtocolVersion, FitFileDataType
from .data import Schema, Data


class FileHeader(Data):
    """Class that decodes a FIT file header."""

    fh_primary_schema = Schema(
        'fh_primary',
        collections.OrderedDict(
            [
                ('header_size', ['UINT8', 1]),
                ('protocol_version', ['UINT8', 1]),
                ('profile_version', ['UINT16', 1]),
                ('data_size', ['UINT32', 1]),
                ('data_type', ['CHAR', 4])
            ]
        )
    )
    fh_optional_schema = Schema(
        'fh_optional',
        collections.OrderedDict([('crc', ['UINT16', 1])])
    )
    profile_version_str = {100 : 'activity', 1602 : 'device'}

    min_file_header_size = 12
    opt_file_header_size = 14
    min_protocol_version = 0x10
    file_data_type = [46, 70, 73, 84]
#    file_data_type = ['.', 'F', 'I', 'T']

    def __init__(self, file):
        """Return a FileHeader instance created by reading data from a Fit file."""
        self.header_size = None
        self.protocol_version = None
        self.profile_version = None
        self.data_size = None
        self.data_type = None
        super().__init__(file, FileHeader.fh_primary_schema, [(FileHeader.fh_optional_schema, self.__decode_secondary)])
        self.__check()

    def __decode_secondary(self):
        return (self.header_size >= FileHeader.opt_file_header_size)

    def __check(self):
        if self.header_size < FileHeader.min_file_header_size:
            raise FitFileBadHeaderSize(f'{self.header_size} < {FileHeader.min_file_header_size}')
        if self.protocol_version < FileHeader.min_protocol_version:
            raise FitFileBadProtocolVersion(f'{self.protocol_version} < {FileHeader.min_protocol_version}')
        if self.data_type != FileHeader.file_data_type:
            raise FitFileDataType(f'{repr(self.data_type)} < {repr(FileHeader.file_data_type)}')

    def __str__(self):
        """Return a string representation of a FileHeader instance."""
        return f'{self.__class__.__name__}(header size {self.header_size} prot ver {self.protocol_version} prof ver {self.profile_version}'
