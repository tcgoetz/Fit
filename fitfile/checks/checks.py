"""Methods for converting metrics from one representation to another."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import datetime


def dt_is_valid(dt):
    """dates in the future are not valid for fit files."""
    return dt <= datetime.datetime.now(datetime.timezone.utc)
