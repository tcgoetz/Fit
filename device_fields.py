"""Objects that represent FIT file device message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from Fit.fields import Field
from Fit.type_fields import BitField
from Fit.enum_fields import EnumField
import Fit.field_enums as fe


class BatteryVoltageField(Field):
    _units = ['v', 'v']
    _conversion_factor = [256.0, 256.0]


class AutoActivityDetectField(BitField):
    bits = {
        0x00000000 : 'none',
        0x00000001 : 'running',
        0x00000002 : 'cycling',
        0x00000004 : 'swimming',
        0x00000008 : 'walking',
        0x00000020 : 'elliptical',
        0x00000400 : 'sedentary',
        0xffffffff : 'invalid'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(name='auto_activity_detect', *args, **kwargs)


class DisplayOrientationField(EnumField):
    enum = fe.DisplayOrientation


class SideField(EnumField):
    enum = fe.Side

    def __init__(self, *args, **kwargs):
        super().__init__(name='side', *args, **kwargs)


class BacklightModeField(EnumField):
    enum = fe.BacklightMode

    def __init__(self, *args, **kwargs):
        super().__init__(name='backlight_mode', *args, **kwargs)


class AntNetworkField(EnumField):
    enum = fe.AntNetwork

    def __init__(self, *args, **kwargs):
        super().__init__(name='ant_network', *args, **kwargs)


class SourceTypeField(EnumField):
    enum = fe.SourceType

    def __init__(self, *args, **kwargs):
        super().__init__(name='source_type', *args, **kwargs)


class AntplusDeviceTypeField(EnumField):
    enum = fe.AntplusDeviceType


class LocalDeviceTypeField(EnumField):
    enum = fe.LocalDeviceType


class UnknownDeviceTypeField(EnumField):
    enum = fe.UnknownDeviceType


class BatteryStatusField(EnumField):
    enum = fe.BatteryStatus

    def __init__(self, *args, **kwargs):
        super().__init__(name='battery_status', *args, **kwargs)


class DeviceType(Field):
    dependant_field_control_fields = ['source_type']

    _source_to_device_type_fields = {
        fe.SourceType.ant          : Field('ant_device_type'),
        fe.SourceType.antplus      : AntplusDeviceTypeField,
        fe.SourceType.local        : LocalDeviceTypeField,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(name='device_type', *args, **kwargs)

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
    enum = fe.AutoSyncFrequency

    def __init__(self, *args, **kwargs):
        super().__init__(name='auto_sync_frequency', *args, **kwargs)


class BodyLocationField(EnumField):
    enum = fe.BodyLocation


class WatchFaceModeField(EnumField):
    enum = fe.WatchFaceMode
