"""Enums that represent FIT file message product field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import re

from .field_enums import FieldEnum, UnknownEnumValue
from .manufacturer import Manufacturer


class MainDeviceType(FieldEnum):
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


class AntplusDeviceType(FieldEnum):
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
    bike_light_main             = 35
    bike_light_shared           = 36
    exd                         = 38
    bike_radar                  = 40
    weight_scale                = 119
    heart_rate                  = 120
    bike_speed_cadence          = 121
    bike_cadence                = 122
    bike_speed                  = 123
    stride_speed_distance       = 124


class LocalDeviceType(FieldEnum):
    """Device types for sub-devices resident on the main device. Like sensors embedded on a watch."""

    gps                             = 0
    accelerometer                   = 3
    barometer                       = 4
    bluetooth_low_energy_chipset    = 8
    wrist_heart_rate                = 10
    sensor_hub                      = 12
    invalid                         = 255


class UnknownDeviceType(UnknownEnumValue):
    """Device type enums for device types that we don't know how to interpret."""
