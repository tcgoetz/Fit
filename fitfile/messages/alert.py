"""Structured data for decoding a FIT file alert message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, StringField, AlertMetricField, SwitchField


alert_message = {
    1 : AlertMetricField('alert_metric'),
    2 : NamedField('value'),
    3 : SwitchField('status'),
    4 : StringField('message'),
    5 : SwitchField('repeat'),
}


# time	uint32			1000		s
# distance	uint32			100		m
# calories	uint32					kcal
