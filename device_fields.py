"""Objects that represent FIT file device message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
from Fit.type_fields import BitField, FloatField
from Fit.enum_fields import EnumField
import Fit.field_enums as fe


class BatteryVoltageField(FloatField):
    """A Field that holds a battery voltage reading for the device."""

    _name = 'battery_voltage'
    _units = 'v'
    _scale = 256.0


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


class AntplusDeviceTypeField(EnumField):

    _name = 'antplus_device_yype'
    _enum = fe.AntplusDeviceType


class LocalDeviceTypeField(EnumField):

    _name = 'local_device_type'
    _enum = fe.LocalDeviceType


class UnknownDeviceTypeField(EnumField):

    _name = 'unknown_device_type'
    _enum = fe.UnknownDeviceType


class BatteryStatusField(EnumField):

    _name = 'battery_status'
    _enum = fe.BatteryStatus


class DeviceType(Field):

    _name = 'device_type'
    _dependant_field_control_fields = ['source_type']

    _source_to_device_type_fields = {
        fe.SourceType.ant          : Field(name='ant_device_type'),
        fe.SourceType.antplus      : AntplusDeviceTypeField,
        fe.SourceType.local        : LocalDeviceTypeField,
    }

    def dependant_field(self, control_value_list):
        """Return a field class that should be used to handle a dependant field."""
        source_type = control_value_list[0]
        if source_type is not None:
            try:
                dependant_field_name = self._source_to_device_type_fields[source_type]
            except Exception:
                dependant_field_name = UnknownDeviceTypeField
        else:
            dependant_field_name = Field
        return dependant_field_name(name='device_type')


class AutoSyncFrequencyField(EnumField):

    _name = 'auto_sync_frequency'
    _enum = fe.AutoSyncFrequency


class BodyLocationField(EnumField):

    _name = 'body_location'
    _enum = fe.BodyLocation


class WatchFaceModeField(EnumField):

    _name = 'watch_face_mode'
    _enum = fe.WatchFaceMode
