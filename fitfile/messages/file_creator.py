"""Structured data for decoding a FIT file event message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import VersionField, BytesField


file_creator_message = {
    0 : VersionField('software_version'),
    1 : VersionField('hardware_version'),
    2 : BytesField('data')
}
