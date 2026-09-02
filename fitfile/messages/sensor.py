"""Structured data for decoding a FIT file sport message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField, StringField, DistanceMillimetersToMetersField, FloatField, ProductField, ManufacturerField, VersionField, BytesField


sensor_message = {
    0 : IntegerField('sensor_id'),
    2 : StringField('name'),
    10 : DistanceMillimetersToMetersField('manual_wheelsize'),
    11 : FloatField('calibration_factor', scale=10.0),
    21 : DistanceMillimetersToMetersField('auto_wheelsize'),
    32 : ProductField(),
    33 : ManufacturerField(),
    34 : VersionField('software_version'),
    50 : BytesField('ble_id')
}
