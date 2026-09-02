"""Structured data for decoding a FIT file data screen message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import Field, IntegerField


data_screen_message = {
    3 : IntegerField('nr_fields'),
    8 : IntegerField('layout'),
    9 : IntegerField('position'),
    10 : Field(name='screen_type'),
}
