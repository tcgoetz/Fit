"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
from Fit.enum_fields import EnumField
from Fit.manufacturer import Manufacturer
from Fit.product import GarminProduct, GarminLocalProduct, ScoscheProduct, WahooFitnessProduct, HealthAndLifeProduct, Unknown680Product, UnknownProduct


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
            return value


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


class Unknown680ProductField(BaseProductField):
    """A field indicating the Wahoo product id of the device used to create the FIT file."""

    _enum = Unknown680Product


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
        Manufacturer.Unknown_680            : Unknown680ProductField,
        Manufacturer.Garmin_local           : GarminLocalProductField,
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
