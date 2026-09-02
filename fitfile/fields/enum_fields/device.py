"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.device import UnknownDeviceType, MainDeviceType, LocalDeviceType, BatteryStatus, AntNetwork, BacklightMode, SourceType, AntplusDeviceType, AutoSyncFrequency, \
    BodyLocation, DateMode, Side, TimeMode, WatchFaceMode, EpoCpeStatus, Satellites, RadarThreatLevelType


class UnknownDeviceTypeField(EnumField):
    """Device type enums for device types that we don't know how to interpret."""

    _name = 'unknown_device_type'
    _enum = UnknownDeviceType


class MainDeviceTypeField(EnumField):
    """Device types for devices connected to the main device via ANT+. Like a external heart rate monitor."""

    _name = 'main_device_type'
    _manufacturer = None
    _product = None
    _enum = MainDeviceType

    def is_invalid(self, value, invalid):
        """Return if the field's value is valid."""
        return False

    def _convert_single(self, value, invalid):
        """Return a device type for the device inferred from its manufactuer and product information."""
        return MainDeviceType.derive_device_type(self._manufacturer, self._product)


class LocalDeviceTypeField(EnumField):
    """Device types for sub-devices resident on the main device. Like sensors embedded on a watch."""

    _name = 'local_device_type'
    _enum = LocalDeviceType


class BatteryStatusField(EnumField):
    """A Field that holds a battery status reading of the device."""

    _name = 'battery_status'
    _enum = BatteryStatus
    _default = BatteryStatus.invalid


class AntNetworkField(EnumField):
    """A field that holds an Ant network type."""

    _name = 'ant_network'
    _enum = AntNetwork


class BacklightModeField(EnumField):
    """A Field that holds the backlight setting for the device."""

    _name = 'backlight_mode'
    _enum = BacklightMode


class SourceTypeField(EnumField):
    """A field that holds the source type of device."""

    _name = 'source_type'
    _enum = SourceType


class AntplusDeviceTypeField(EnumField):
    """Device types for devices connected to the main device via ANT+. Like a external heart rate monitor."""

    _name = 'antplus_device_type'
    _enum = AntplusDeviceType


class AutoSyncFrequencyField(EnumField):
    """A field that holds the maxiimum amount of time before the device automatically syncs with the cloud."""

    _name = 'auto_sync_frequency'
    _enum = AutoSyncFrequency


class BodyLocationField(EnumField):
    """A field that identifies a location of a device on the body."""

    _name = 'body_location'
    _enum = BodyLocation


class DateModeField(EnumField):

    _name = 'date_mode'
    _enum = DateMode


class SideField(EnumField):
    """A Field that holds the left/right wrist setting for the device."""

    _name = 'side'
    _enum = Side


class TimeModeField(EnumField):

    _name = 'time_mode'
    _enum = TimeMode


class WatchFaceModeField(EnumField):
    """A field that identifies the mode the watch face is in."""

    _name = 'watch_face_mode'
    _enum = WatchFaceMode


class EpoCpeStatusField(EnumField):
    """A field that identifies the ."""

    _name = 'epo_cpe_status'
    _enum = EpoCpeStatus


class SatellitesField(EnumField):
    """A field that identifies the ."""

    _name = 'satellites'
    _enum = Satellites


class RadarThreatLevelTypeField(EnumField):
    """A field that identifies the mode the ."""

    _name = 'satellites'
    _enum = RadarThreatLevelType
