"""Library for parsing FIT files and returning them as lists of messages dictionaries."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# flake8: noqa

from .field_enums import UnknownEnumValue, FieldEnum, FuzzyFieldEnum, Switch, FitBaseUnit, DisplayMeasure, DisplayHeart, DisplayPosition, DisplayOrientation, Side, BacklightMode, \
    AntNetwork, SourceType, BatteryStatus, AutoSyncFrequency, BodyLocation, Gender, HeartRateZoneCalc, PowerCalc, Language, DateMode, TimeMode, Activity, ActivityType, Event, EventType, \
    LapTrigger, SessionTrigger, PersonalRecordType, GoalType, GoalRecurrence, GoalSource, WatchFaceMode, ClimbProEvent, HeartRateZonesTimerType, HeartRateZonesMethod, name_for_enum, \
    SleepActivityLevel