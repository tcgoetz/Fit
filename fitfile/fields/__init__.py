"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa


from .field import Field, NamedField, UnknownField, LeftRightBalanceField, PercentField, BytePercentField, MessageIndexField, VersionField

from .activity import ActivityBasedCyclesField, ActivityClassField, IntensityField, ActivityTypeIntensityField, SportBasedCyclesField, CadenceField, StepsCadenceField, \
    StrokesCadenceField, SportBasedCadenceField, WorkField, WorkoutCapabilitiesField

from .time import TimestampField, TimeMsField, TimeSField, TimeOffsetField, TimeHourField, TimeMinField, TimeOfDayField
from .sport import CyclesField, StepsField, StrokesField, CyclesDistanceField, FractionalCadenceField, PowerField, TrainingEffectField, ClimbingGrade, ClimbingRouteComleted, FractionalCyclesField


from .calories import CaloriesField, CaloriesDayField, CyclesCaloriesField
from .data import *
from .dev import *
from .device import *
from .objects import *
from .records import *
from .types import *

#
# field_enums
#
from .field_enums.activity import Sport, SubSport, Spo2MeasurementType
from .field_enums.device import BatteryStatus, MainDeviceType
from .field_enums.event import Event, EventType
from .field_enums.file_type import FileType
from .field_enums.heart_rate import HeartRateZoneCalc, HeartRateZonesTimerType, HeartRateVarianceStatus
from .field_enums.manufacturer import Manufacturer
from .field_enums.product import GarminProduct
from .field_enums.sleep import SleepActivityLevel
from .field_enums.switch import Switch
from .field_enums.user_profile import Gender


#
# enum_fields
#

# from .enum_fields.enum import Enum

from .enum_fields.activity import Activity, ActivityField, ActivityType, ActivityTypeField, SportField, SubSportField, LapTriggerField, SessionTriggerField, PowerCalcField, \
    PowerZoneCalcField, BenefitField, AutoLapModeField, PowerAveragingField, Spo2MeasurementTypeField
from .enum_fields.alert import AlertMetricField
from .enum_fields.climb import ClimbProEventField
from .enum_fields.user_profile import DisplayHeartField, DisplayMeasureField, DisplayOrientation, DisplayPositionField, DisplayOrientationField, LanguageField, GenderField
from .enum_fields.device import UnknownDeviceTypeField, MainDeviceTypeField, LocalDeviceTypeField, AntNetworkField, BacklightModeField, SourceTypeField, BatteryStatusField, \
    DateModeField, BodyLocationField, AutoSyncFrequencyField, AntplusDeviceTypeField, SideField, TimeModeField, WatchFaceModeField, EpoCpeStatusField, SatellitesField, \
    RadarThreatLevelTypeField
from .enum_fields.event import EventField, EventTypeField
from .enum_fields.file_type import FileType, FileTypeField
from .enum_fields.fit_base_unit import FitBaseUnitField
from .enum_fields.goal import GoalType, GoalTypeField, GoalSourceField, GoalRecurrenceField, PersonalRecordTypeField
from .enum_fields.heart_rate import HeartRateZoneCalcField, HeartRateZoneCalcField, HeartRateZonesTimerTypeField, HeartRateVarianceStatusField
from .enum_fields.manufacturer import Manufacturer, ManufacturerField
from .enum_fields.product import ProductField, GarminProductField
from .enum_fields.settings import VolumeUnitsField, SelfEvaluationStatusField, TouchStatusField, RunningPowerModeField, ClimbProModeModeField, ClimbDetectionField, \
    ClimbProTerrainField, TapSensitivityField, AutoScrollModeField, AutoPauseSettingField
from .enum_fields.sleep import SleepActivityLevelField, SleepDisruptionsSeveritylField
from .enum_fields.switch import SwitchField
