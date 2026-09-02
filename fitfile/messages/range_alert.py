"""Structured data for decoding a FIT file range alert message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField


range_alert_message = {
    1 : NamedField('zone_metric'),
    2 : NamedField('low_status'),
    3 : NamedField('low_value'),
    4 : NamedField('high_status'),
    5 : NamedField('high_value'),
}


# speed	uint16			1000		m/s			metric	speed
# cadence	uint16					rpm			metric	cadence
# power	uint16					watts			metric	power
# elevation	uint16			5	500	m/s			metric	elevation
