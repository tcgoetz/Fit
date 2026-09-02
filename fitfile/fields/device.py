"""Objects that represent FIT file device message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from . import Field
from .types import BitField, FloatField
from .enum_fields.device import MainDeviceTypeField, LocalDeviceTypeField, AntplusDeviceTypeField, UnknownDeviceTypeField
from .field_enums.device import SourceType


class BatteryVoltageField(FloatField):
    """A Field that holds a battery voltage reading for the device."""

    _name = 'battery_voltage'
    _units = 'v'
    _scale = 256.0


class AutoActivityDetectField(BitField):
    """A filed that contains a mask of activitiy types that will automatically be tracked."""

    _name = 'auto_activity_detect'
    _bits = {
        0x00000000: 'none',
        0x00000001: 'running',
        0x00000002: 'cycling',
        0x00000004: 'swimming',
        0x00000008: 'walking',
        0x00000020: 'elliptical',
        0x00000400: 'sedentary',
        0xffffffff: 'invalid'
    }


class DeviceTypeField(Field):
    """Wrapper field for device type dependant fields."""

    _name = 'device_type'
    _dependant_field_control_fields = ['source_type', 'device_type', 'manufacturer', 'product']

    _source_to_device_type_fields = {
        SourceType.ant: Field,
        SourceType.antplus: AntplusDeviceTypeField,
        SourceType.local: LocalDeviceTypeField,
    }

    def dependant_field(self, control_value_list):
        """Return a field class that should be used to handle a dependant field."""
        source_type = control_value_list[0]
        device_type = control_value_list[1]
        manufacturer = control_value_list[2]
        product = control_value_list[3]
        if source_type is not None:
            if source_type is SourceType.local and device_type is None:
                dependant_field = MainDeviceTypeField(manufacturer=manufacturer, product=product, name='device_type')
            else:
                try:
                    dependant_field = self._source_to_device_type_fields[source_type](name='device_type')
                except Exception:
                    dependant_field = UnknownDeviceTypeField(name='device_type')
        else:
            dependant_field = Field(name='device_type')
        return dependant_field
