"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import re

from .enum import Enum, UnknownEnumValue
from .manufacturer import Manufacturer


class UnknownDeviceType(UnknownEnumValue):
    """Device type enums for device types that we don't know how to interpret."""


class MainDeviceType(Enum):
    """Device type for the main device."""

    fitness_tracker = 0
    bike_gps        = 1
    standalone_gps  = 2
    software        = 3
    other           = 254
    invalid         = 255

    @classmethod
    def derive_device_type(cls, manufacturer, product):
        """Return a device type for the device inferred from its manufactuer and product information."""
        device_type_mappings = {
            Manufacturer.Garmin: {
                cls.fitness_tracker  : r'Vivo|Forerunner|Fenix',
                cls.bike_gps         : r'Edge',
                cls.standalone_gps   : r'GPSMap',
                cls.software         : r'connect|Training_Center'
            }
        }
        if manufacturer in device_type_mappings:
            for device_type, regex in device_type_mappings[manufacturer].items():
                if re.search(regex, product.name, re.IGNORECASE):
                    return device_type
        return cls.other


class LocalDeviceType(Enum):
    """Device types for sub-devices resident on the main device. Like sensors embedded on a watch."""

    gps                             = 0
    accelerometer                   = 3
    barometer                       = 4
    bluetooth_low_energy_chipset    = 8
    wrist_heart_rate                = 10
    sensor_hub                      = 12
    invalid                         = 255


class BatteryStatus(Enum):
    """An enum that defines the state of a battery."""

    new = 1
    good = 2
    ok = 3
    low = 4
    critical = 5
    charging = 6
    unknown = 7
    invalid = 255


class AntNetwork(Enum):
    public  = 0
    antplus = 1
    antfs   = 2
    private = 3
    invalid = 255


class BacklightMode(Enum):
    off = 0
    manual = 1
    key_and_messages = 2
    auto_brightness = 3
    smart_notifications = 4
    key_and_messages_night = 5
    key_and_messages_and_smart_notifications = 6
    invalid = 255


class SourceType(Enum):
    ant = 0
    antplus = 1
    bluetooth = 2
    bluetooth_low_energy = 3
    wifi = 4
    local = 5
    invalid = 255


class AntplusDeviceType(Enum):
    """Device types for devices connected to the main device via ANT+. Like a external heart rate monitor."""

    antfs                       = 1
    bike_power                  = 11
    environment_sensor_legacy   = 12
    multi_sport_speed_distance  = 15
    control                     = 16
    fitness_equipment           = 17
    blood_pressure              = 18
    geocache_node               = 19
    light_electric_vehicle      = 20
    env_sensor                  = 25
    racquet                     = 26
    control_hub                 = 27
    run                         = 30
    muscle_oxygen               = 31
    shifting                    = 34
    bike_light_main             = 35
    bike_light_shared           = 36
    exd                         = 38
    bike_radar                  = 40
    bike_aero                   = 46
    weight_scale                = 119
    heart_rate                  = 120
    bike_speed_cadence          = 121
    bike_cadence                = 122
    bike_speed                  = 123
    stride_speed_distance       = 124


class AutoSyncFrequency(Enum):
    never = 0
    occasionally = 1
    frequent = 2
    once_a_day = 3
    remote = 4
    invalid = 255


class BodyLocation(Enum):
    left_leg = 0
    left_calf = 1
    left_shin = 2
    left_hamstring = 3
    left_quad = 4
    left_glute = 5
    right_leg = 6
    right_calf = 7
    right_shin = 8
    right_hamstring = 9
    right_quad = 10
    right_glut = 11
    torso_back = 12
    left_lower_back = 13
    left_upper_back = 14
    right_lower_back = 15
    right_upper_back = 16
    torso_front = 17
    left_abdomen = 18
    left_chest = 19
    right_abdomen = 20
    right_chest = 21
    left_arm = 22
    left_shoulder = 23
    left_bicep = 24
    left_tricep = 25
    left_brachioradialis = 26
    left_forearm_extensors = 27
    right_arm = 28
    right_shoulder = 29
    right_bicep = 30
    right_tricep = 31
    right_brachioradialis = 32
    right_forearm_extensors = 33
    neck = 34
    throat = 35
    waist_mid_back = 36
    waist_front = 37
    waist_left = 38
    waist_right = 39
    invalid = 255


class DateMode(Enum):
    day_month   = 0
    month_day   = 1
    invalid     = 255


class Side(Enum):
    """An enum that defines what side of the body a device is on."""

    right = 0
    left = 1
    invalid = 255


class TimeMode(Enum):
    twelve_hour             = 0
    twentyfour_hour         = 1
    military                = 2
    twelve_hour_secs        = 3
    twentyfour_hour_secs    = 4
    utc                     = 5
    invalid                 = 255


class WatchFaceMode(Enum):
    """A enum that describes a mode of the watch face."""

    digital         = 0
    analog          = 1
    connect_iq      = 2
    disabled        = 3


class EpoCpeStatus(Enum):
    """A enum that describes extended prediction orbit statu."""

    expired         = 0
    current         = 1


class Satellites(Enum):
    """A enum that describes which satellites are enabled."""

    off             = 0
    gps_only        = 1
    gps_glonass     = 2
    ultra_trac      = 3
    gps_galileo     = 5
    all_systems     = 7
    all_multi_band  = 8
    auto_select     = 9


class RadarThreatLevelType(Enum):
    """A enum that describes which radar threat level are enabled."""

    threat_unknown          = 0
    threat_none             = 1
    threat_approaching      = 2
    threat_approaching_fast = 3


class GpsEventType(Enum):
    signal_lost = 3
    ultra_trac_trigger = 11
    mode_change = 49
