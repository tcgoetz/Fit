"""Structured data for decoding a FIT file power zone message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import PowerField, StringField


power_zone_message = {
    1 : PowerField('high_value'),
    2 : StringField('name'),
}
