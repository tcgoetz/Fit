"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import EnumField
from ..field_enums.settings import VolumeUnits, SelfEvaluationStatus, TouchStatus, RunningPowerMode, ClimbProMode, ClimbDetection, ClimbProTerrain, TapSensitivity


class VolumeUnitsField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'volume_units'
    _enum = VolumeUnits


class SelfEvaluationStatusField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'self_evaluation'
    _enum = SelfEvaluationStatus


class TouchStatusField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'touch_status'
    _enum = TouchStatus


class RunningPowerModeField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'running_power_mode'
    _enum = RunningPowerMode


class ClimbProModeModeField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'climb_pro_mode'
    _enum = ClimbProMode


class ClimbDetectionField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'climb_detection'
    _enum = ClimbDetection


class ClimbProTerrainField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'climb_pro_terrain'
    _enum = ClimbProTerrain


class TapSensitivityField(EnumField):
    """A field that contains Enum of values used to encode ."""

    _name = 'tap_sensitivity'
    _enum = TapSensitivity
