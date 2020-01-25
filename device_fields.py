"""Objects that represent FIT file device message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
from Fit.type_fields import BitField, FloatField
from Fit.enum_fields import EnumField
import Fit.field_enums as fe
import Fit.device_enums as de


class BatteryVoltageField(FloatField):
    """A Field that holds a battery voltage reading for the device."""

    _name = 'battery_voltage'
    _units = 'v'
    _scale = 256.0


class BatteryStatusField(EnumField):
    """A Field that holds a battery status reading of the device."""

    _name = 'battery_status'
    _enum = fe.BatteryStatus


class AutoActivityDetectField(BitField):

    _name = 'auto_activity_detect'
    _bits = {
        0x00000000 : 'none',
        0x00000001 : 'running',
        0x00000002 : 'cycling',
        0x00000004 : 'swimming',
        0x00000008 : 'walking',
        0x00000020 : 'elliptical',
        0x00000400 : 'sedentary',
        0xffffffff : 'invalid'
    }


class DisplayOrientationField(EnumField):
    """A Field that holds the display orientation setting for the device."""

    _name = 'display_orientation'
    _enum = fe.DisplayOrientation


class SideField(EnumField):
    """A Field that holds the left/right wrist setting for the device."""

    _name = 'side'
    _enum = fe.Side


class BacklightModeField(EnumField):
    """A Field that holds the backlight setting for the device."""

    _name = 'backlight_mode'
    _enum = fe.BacklightMode


class AntNetworkField(EnumField):

    _name = 'ant_network'
    _enum = fe.AntNetwork


class SourceTypeField(EnumField):

    _name = 'source_type'
    _enum = fe.SourceType


class MainDeviceTypeField(EnumField):
    """Device types for devices connected to the main device via ANT+. Like a external heart rate monitor."""

    _name = 'main_device_type'
    _enum = de.MainDeviceType

    def is_invalid(self, value, invalid):
        """Return if the field's value is valid."""
        return False

    def _convert_single(self, value, invalid):
        """Return a device type for the device inferred from its manufactuer and product information."""
        return de.MainDeviceType.derive_device_type(self._manufacturer, self._product)


class AntplusDeviceTypeField(EnumField):
    """Device types for devices connected to the main device via ANT+. Like a external heart rate monitor."""

    _name = 'antplus_device_type'
    _enum = de.AntplusDeviceType


class LocalDeviceTypeField(EnumField):
    """Device types for sub-devices resident on the main device. Like sensors embedded on a watch."""

    _name = 'local_device_type'
    _enum = de.LocalDeviceType


class UnknownDeviceTypeField(EnumField):
    """Device type enums for device types that we don't know how to interpret."""

    _name = 'unknown_device_type'
    _enum = de.UnknownDeviceType


class DeviceTypeField(Field):
    """Wrapper field for device type dependant fields."""

    _name = 'device_type'
    _dependant_field_control_fields = ['source_type', 'device_type', 'manufacturer', 'product']

    _source_to_device_type_fields = {
        fe.SourceType.ant          : Field,
        fe.SourceType.antplus      : AntplusDeviceTypeField,
        fe.SourceType.local        : LocalDeviceTypeField,
    }

    def dependant_field(self, control_value_list):
        """Return a field class that should be used to handle a dependant field."""
        source_type = control_value_list[0]
        device_type = control_value_list[1]
        manufacturer = control_value_list[2]
        product = control_value_list[3]
        if source_type is not None:
            if source_type is fe.SourceType.local and device_type is None:
                dependant_field = MainDeviceTypeField(manufacturer=manufacturer, product=product, name='device_type')
            else:
                try:
                    dependant_field = self._source_to_device_type_fields[source_type](name='device_type')
                except Exception:
                    dependant_field = UnknownDeviceTypeField(name='device_type')
        else:
            dependant_field = Field(name='device_type')
        return dependant_field


class AutoSyncFrequencyField(EnumField):

    _name = 'auto_sync_frequency'
    _enum = fe.AutoSyncFrequency


class BodyLocationField(EnumField):

    _name = 'body_location'
    _enum = fe.BodyLocation


class WatchFaceModeField(EnumField):

    _name = 'watch_face_mode'
    _enum = fe.WatchFaceMode
