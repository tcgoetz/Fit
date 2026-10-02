"""Structured data for decoding a FIT file sport message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import IntegerField, StringField, DistanceMillimetersToMetersField, FloatField, ProductField, ManufacturerField, VersionField, BytesField, CrankLengthField, \
    WeightField, NamedField, WeightGramsField


sensor_message = {
    0 : IntegerField('sensor_id'),
    #
    2 : StringField('name'),
    3 : IntegerField('status'),
    #
    6 : IntegerField('wheel_calibration'),
    7 : IntegerField('power_calibration'),
    #
    9 : CrankLengthField('crank_length'),
    10 : DistanceMillimetersToMetersField('manual_wheelsize'),
    11 : FloatField('calibration_factor', scale=10.0),
    #
    17 : IntegerField('gears_front_count'),
    18 : IntegerField('gears_front'),
    19 : IntegerField('gears_rear_count'),
    20 : IntegerField('gears_rear'),
    21 : DistanceMillimetersToMetersField('auto_wheelsize'),
    #
    25 : FloatField('gear_ratio', scale=100),
    26 : WeightField('bike_weight'),
    #
    32 : ProductField(),
    33 : ManufacturerField(),
    34 : VersionField('software_version'),
    #
    41 : NamedField('cycling_beam_focus'),
    #
    43 : IntegerField('cycling_dynamics'),
    #
    45 : IntegerField('use_for_speed'),
    46 : IntegerField('use_for_distance'),
    #
    49 : IntegerField('cycling_beam_intensity'),
    50 : BytesField('ble_id'),
    51 : IntegerField('connection_type'),
    52 : IntegerField('sensor_type'),
    #
    55 : WeightGramsField('chain_weight'),
    56 : DistanceMillimetersToMetersField('chain_length'),
    57 : DistanceMillimetersToMetersField('span_length'),
    #
    91 : StringField('product_name'),
    #
    93 : BytesField('uuid')
}
