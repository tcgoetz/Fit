"""Enums that represent FIT file message product field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from ..field import Field
from .enum import EnumField
from ..field_enums.enum import UnknownEnumValue
from ..field_enums.product import GarminProduct, GarminLocalProduct, WahooFitnessProduct, ScoscheProduct, HealthAndLifeProduct
from .manufacturer import Manufacturer


class UnknownProduct(UnknownEnumValue):
    """Unknown product codes used in FIT files."""


class BaseProductField(EnumField):
    """A field indicating the product id of the device used to create the FIT file."""

    _name = 'product'


class GarminProductField(BaseProductField):
    """A field indicating the Garmin product id of the device used to create the FIT file."""

    _enum = GarminProduct


class GarminLocalProductField(BaseProductField):
    """A field indicating the Garmin local product id of the device used to create the FIT file."""

    _enum = GarminLocalProduct


class WahooFitnessProductField(BaseProductField):
    """A field indicating the Wahoo product id of the device used to create the FIT file."""

    _enum = WahooFitnessProduct


class ScoscheProductField(BaseProductField):
    """A field indicating the Scosche product id of the device used to create the FIT file."""

    _enum = ScoscheProduct


class HealthAndLifeProductField(BaseProductField):
    """A field indicating the Scosche product id of the device used to create the FIT file."""

    _enum = HealthAndLifeProduct


class UnknownProductField(BaseProductField):
    """A field indicating the undocumented product id of the device used to create the FIT file."""

    _enum = UnknownProduct


class ProductField(Field):
    """A field indicating the product id of the device used to create the FIT file."""

    _name = 'product'
    _dependant_field_control_fields = ['manufacturer']

    _manufacturer_to_product_fields = {
        Manufacturer.Garmin                 : GarminProductField,
        Manufacturer.Dynastream             : GarminProductField,
        Manufacturer.Dynastream_OEM         : GarminProductField,
        Manufacturer.Wahoo_Fitness          : WahooFitnessProductField,
        Manufacturer.Scosche                : ScoscheProductField,
        Manufacturer.Health_and_Life        : HealthAndLifeProductField,
        Manufacturer.Garmin_local           : GarminLocalProductField,
        Manufacturer.Garmin_local_154       : GarminLocalProductField,
        Manufacturer.Garmin_local_218       : GarminLocalProductField,
        Manufacturer.unknown                : UnknownProductField,
        Manufacturer.invalid                : GarminProductField,
    }

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        manufacturer = control_value_list[0]
        try:
            dependant_field_name = self._manufacturer_to_product_fields[manufacturer]
        except Exception:
            dependant_field_name = UnknownProductField
        return dependant_field_name()
