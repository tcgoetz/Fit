"""Structured data for decoding a FIT file zones target message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, HeartRateZoneCalcField, PowerCalcField, HeartRateField


zones_target_message = {
    1 : HeartRateField('max_heart_rate'),
    2 : HeartRateField('threshold_heart_rate'),
    3 : NamedField('functional_threshold_power'),
    5 : HeartRateZoneCalcField(),
    7 : PowerCalcField()
}
