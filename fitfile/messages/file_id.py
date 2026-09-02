"""Structured data for decoding a FIT file id message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import FileTypeField, ManufacturerField, ProductField, IntegerField, StringField, TimestampField


file_id_message = {
    0 : FileTypeField('type'),
    1 : ManufacturerField(),
    2 : ProductField(),
    3 : IntegerField('serial_number'),
    4 : TimestampField('time_created', utc=True),
    5 : IntegerField('number'),
    8 : StringField('product_name')
}
