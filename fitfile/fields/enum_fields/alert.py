"""Objects that represent FIT file alert fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.alert import AlertMetric


class AlertMetricField(EnumField):

    _name = 'time_mode'
    _enum = AlertMetric
