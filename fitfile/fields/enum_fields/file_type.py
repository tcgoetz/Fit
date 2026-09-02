"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.file_type import FileType


class FileTypeField(EnumField):
    """A field that indicates the FIT file type."""

    _name = 'file_type'
    _enum = FileType
