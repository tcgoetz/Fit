"""Enums that represent FIT file message manufacturer field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from .enum import EnumField
from ..field_enums.manufacturer import Manufacturer


class ManufacturerField(EnumField):
    """A field indicating the manufacturer of the device used to create the FIT file."""

    _name = 'manufacturer'
    _enum = Manufacturer

    def _convert_single(self, value, invalid):
        try:
            return self._enum(value)
        except Exception:
            if value >= Manufacturer.Garmin_local_start.value:
                return Manufacturer.Garmin_local
            return Manufacturer.unknown
