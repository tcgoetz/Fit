"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
from Fit.enum_fields import EnumField
import Fit.field_enums as fe


class ManufacturerField(EnumField):
    """A field indicating the manufacturer of the device used to create the FIT file."""

    enum = fe.Manufacturer

    def __init__(self, *args, **kwargs):
        super().__init__(name='manufacturer', *args, **kwargs)

    def _convert_single(self, value, invalid):
        try:
            return self.enum(value)
        except Exception:
            if value >= fe.Manufacturer.Garmin_local_start.value:
                return fe.Manufacturer.Garmin_local
            return value


class BaseProductField(EnumField):
    """A field indicating the product id of the device used to create the FIT file."""

    def __init__(self, *args, **kwargs):
        super().__init__(name='product', *args, **kwargs)


class GarminProductField(BaseProductField):
    """A field indicating the Garmin product id of the device used to create the FIT file."""

    enum = fe.GarminProduct


class GarminLocalProductField(BaseProductField):
    """A field indicating the Garmin local product id of the device used to create the FIT file."""

    enum = fe.GarminLocalProduct


class ScoscheProductField(BaseProductField):
    """A field indicating the Scosche product id of the device used to create the FIT file."""

    enum = fe.ScoscheProduct


class WahooFitnessProductField(BaseProductField):
    """A field indicating the Wahoo product id of the device used to create the FIT file."""

    enum = fe.WahooFitnessProduct


class UnknownProductField(BaseProductField):
    """A field indicating the undocumented product id of the device used to create the FIT file."""

    enum = fe.UnknownProduct


class ProductField(Field):
    """A field indicating the product id of the device used to create the FIT file."""

    dependant_field_control_fields = ['manufacturer']

    _manufacturer_to_product_fields = {
        fe.Manufacturer.Garmin                 : GarminProductField,
        fe.Manufacturer.Dynastream             : GarminProductField,
        fe.Manufacturer.Dynastream_OEM         : GarminProductField,
        fe.Manufacturer.Scosche                : ScoscheProductField,
        fe.Manufacturer.Wahoo_Fitness          : WahooFitnessProductField,
        fe.Manufacturer.Garmin_local           : GarminLocalProductField,
        fe.Manufacturer.invalid                : GarminProductField,
    }

    def dependant_field(self, control_value_list):
        """Return a dependant field instance given the control field values."""
        manufacturer = control_value_list[0]
        try:
            dependant_field_name = self._manufacturer_to_product_fields[manufacturer]
        except Exception:
            dependant_field_name = UnknownProductField
        return dependant_field_name()
