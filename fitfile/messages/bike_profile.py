"""Structured data for decoding a FIT file bike profile message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, PercentField, IntegerField, BoolField, StringField, SportField, SubSportField, WeightField, DistanceCentimetersToMetersField, \
    DistanceMillimetersToMetersField


bike_profile_message = {
    0 : StringField('name'),
    1 : SportField(),
    2 : SubSportField(),
    3 : DistanceCentimetersToMetersField('odometer'),
    4 : NamedField('bike_spd_ant_id'),
    5 : NamedField('bike_cad_ant_id'),
    6 : NamedField('bike_spdcad_ant_id'),
    7 : NamedField('bike_power_ant_id'),
    8 : DistanceMillimetersToMetersField('custom_wheelsize'),
    9 : DistanceMillimetersToMetersField('auto_wheelsize'),
    10 : WeightField('bike_weight'),
    11 : PercentField('power_cal_factor'),
    12 : BoolField('auto_wheel_cal'),
    13 : BoolField('auto_power_zero'),
    14 : IntegerField('id'),
    15 : BoolField('spd_enabled'),
    16 : BoolField('cad_enabled'),
    17 : BoolField('spdcad_enabled'),
    18 : BoolField('power_enabled'),
    19 : DistanceMillimetersToMetersField('crank_length'),
    20 : BoolField('enabled'),
    21 : NamedField('bike_spd_ant_id_trans_type'),
    22 : NamedField('bike_cad_ant_id_trans_type'),
    23 : NamedField('bike_spdcad_ant_id_trans_type'),
    24 : NamedField('bike_power_ant_id_trans_type'),
    37 : NamedField('odometer_rollover'),
}
