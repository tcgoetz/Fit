"""Enums that represent FIT file message field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

import enum


def name_for_enum(enum_instance):
    """Return the name if variable is enum or UnknownEnumValue."""
    return getattr(enum_instance, 'name', enum_instance)


class UnknownEnumValue():
    """Returned when a value can not be cast to an FieldEnum."""

    def __init__(self, value):
        """Return a UnknownEnumValue instance."""
        self.value = value
        self.name = f'{type(self).__name__}_{value}'

    @classmethod
    def from_string(cls, string, default=None):
        """Return a UnknownEnumValue instance created from a string."""
        return cls(string)

    def __eq__(self, other):
        """Test two UnknownEnumValue instances for equivelence."""
        return (other and (isinstance(other, UnknownEnumValue) and self.value == other.value)
                or (not isinstance(other, UnknownEnumValue) and self.value == other))

    def __ne__(self, other):
        """Test two UnknownEnumValue instances for equivelence."""
        return not self.__eq__(other)

    def __hash__(self):
        """Return a hash value for a UnknownEnumValue instance."""
        return self.value

    def __repr__(self):
        """Return a string representation of a UnknownEnumValue instance."""
        return f'<{type(self).__name__}.{self.name}: {self.value}>'


class FieldEnum(enum.Enum):
    """A enum representing a FIT file message field value."""

    @classmethod
    def _from_string(cls, string):
        try:
            return cls(string)
        except Exception:
            return getattr(cls, string)

    @classmethod
    def strict_from_string(cls, string):
        """Return an instance of FieldEnum instantiated with string."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            return None

    @classmethod
    def from_string(cls, string, default=None):
        """Return an instance of FieldEnum instantiated with string or an instancxe of UnknownEnumValue if not found."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            if default:
                return default
            return UnknownEnumValue(string)


class CaseInsensitiveFieldEnum(FieldEnum):
    """A enum representing a field value that can be instantiated with a case insensitive match."""

    @classmethod
    def from_string_ext(cls, string):
        """Return an instance of FieldEnum instantiated with string using a case insensitive match."""
        for name, value in cls.__members__.items():
            if name.lower() == str(string).lower():
                return value
        return UnknownEnumValue(string)

    @classmethod
    def from_string(cls, string, default=None):
        """Return an instance of FieldEnum instantiated with string."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            if default:
                return default
            return cls.from_string_ext(string)


class FuzzyFieldEnum(FieldEnum):
    """A enum representing a field value that can be instantiated with a fuzzy match."""

    @classmethod
    def from_string_ext(cls, string):
        """Return an instance of FieldEnum instantiated with string using a fuzzy match."""
        for name, value in cls.__members__.items():
            if name.lower() in str(string).lower():
                return value
        return UnknownEnumValue(string)

    @classmethod
    def from_string(cls, string, default=None):
        """Return an instance of FieldEnum instantiated with string."""
        try:
            return cls._from_string(string)
        except (AttributeError, TypeError):
            if default:
                return default
            return cls.from_string_ext(string)


class Switch(FieldEnum):
    """An enum representing a FIT switch field value."""

    off         = 0
    on          = 1
    auto        = 2
    invalid     = 255


class FitBaseUnit(FieldEnum):
    other       = 0
    kg          = 1
    lb          = 2
    invalid     = 255


class DisplayMeasure(FuzzyFieldEnum):
    metric      = 0
    statute     = 1
    nautical    = 2
    invalid     = 255


class DisplayHeart(FieldEnum):
    """An enum that defines how heart rate will be displayed."""

    bpm     = 0
    max     = 1
    reserve = 2
    invalid = 255


class DisplayPosition(FieldEnum):
    """An enum that defines how position data will be displayed."""

    degree = 0
    dregree_minute = 1
    degree_minute_second = 2
    australian_grid = 3
    british_grid = 4
    dutch_grid = 5
    hugarian_grid = 6
    finish_grid = 7
    german_grid = 8
    icelandic_grid = 9
    indonesian_equatorial = 10
    indonesian_irian = 11
    indonesian_southern = 12
    india_zone_0 = 13
    india_zone_ia = 14
    india_zone_ib = 15
    india_zone_iia = 16
    india_zone_iib = 17
    india_zone_iiia = 18
    india_zone_iiib = 19
    india_zone_iva = 20
    india_zone_ivb = 21
    irish_traverse = 22
    irish_grid = 23
    loran = 24
    maidenhead_grid = 25
    mgrs_grid = 26
    new_zealand_grid = 27
    new_zealand_traverse = 28
    qatar_grid = 29
    modified_swedish_grid = 30
    swedish_grid = 31
    south_african_grid = 32
    swiss_grid = 33
    tiawan_grid = 34
    united_stated_grid = 35
    utm_ups_grid = 36
    west_malayan = 37
    borneo_rso = 38
    estonian_grid = 39
    latvian_grid = 40
    swedish_ref_99_grid = 41
    invalid = 255


class DisplayOrientation(FieldEnum):
    auto = 0
    portrait = 1
    landscape = 2
    portrait_flipped = 3
    landscape_flipped = 4
    invalid = 255


class Side(FieldEnum):
    """An enum that defines what side of the body a device is on."""

    right = 0
    left = 1
    invalid = 255


class BacklightMode(FieldEnum):
    off = 0
    manual = 1
    key_and_messages = 2
    auto_brightness = 3
    smart_notifications = 4
    key_and_messages_night = 5
    key_and_messages_and_smart_notifications = 6
    invalid = 255


class AntNetwork(FieldEnum):
    public  = 0
    antplus = 1
    antfs   = 2
    invalid = 255


class SourceType(FieldEnum):
    ant = 0
    antplus = 1
    bluetooth = 2
    bluetooth_low_energy = 3
    wifi = 4
    local = 5
    invalid = 255


class BatteryStatus(FieldEnum):
    """An enum that defines the state of a battery."""

    new = 1
    good = 2
    ok = 3
    low = 4
    critical = 5
    charging = 6
    unknown = 7
    invalid = 255


class AutoSyncFrequency(FieldEnum):
    never = 0
    occasionally = 1
    frequent = 2
    once_a_day = 3
    remote = 4
    invalid = 255


class BodyLocation(FieldEnum):
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


class Gender(CaseInsensitiveFieldEnum):
    female = 0
    male = 1


class HeartRateZoneCalc(FieldEnum):
    custom = 0
    percent_max_hr = 1
    percent_hrr = 2
    invalid = 255


class PowerCalc(FieldEnum):
    custom = 0
    percent_ftp = 1
    invalid = 255


class Language(FieldEnum):
    English = 0
    French = 1
    Italian = 2
    German = 3
    Spanish = 4
    Croation = 5
    Czech = 6
    Danish = 7
    Dutch = 8
    Finnish = 9
    Greek = 10
    Hungarian = 11
    Norwegian = 12
    Polish = 13
    Portuguese = 14
    Slovakian = 15
    Slovenian = 16
    Swedish = 17
    Russian = 18
    Turkish = 19
    Latvian = 20
    Ukranian = 21
    Arabic = 22
    Farsi = 23
    Bulgarian = 24
    Romanian = 25
    Chinese = 26
    Japanese = 27
    Korean = 28
    Taiwanese = 29
    Thai = 30
    Hebrew = 31
    Brazialn_Portuguese = 32
    Indonesian = 33
    Maylasian = 34
    Vietnamese = 35
    Burmese = 36
    Mongolian = 37
    Custom = 254
    Invalid = 255


class DateMode(FieldEnum):
    day_month   = 0
    month_day   = 1
    invalid     = 255


class TimeMode(FieldEnum):
    twelve_hour             = 0
    twentyfour_hour         = 1
    military                = 2
    twelve_hour_secs        = 3
    twentyfour_hour_secs    = 4
    utc                     = 5
    invalid                 = 255


class Activity(FieldEnum):
    manual              = 0
    auto_multi_sport    = 1


class ActivityType(FieldEnum):
    generic             = 0
    running             = 1
    cycling             = 2
    transition          = 3
    fitness_equipment   = 4
    swimming            = 5
    walking             = 6
    sedentary           = 7
    stop_disable        = 8
    unknown             = 9
    all                 = 245
    invalid             = 255


class Event(FieldEnum):
    timer = 0
    workout = 3
    workout_step = 4
    power_down = 5
    power_up = 6
    off_course = 7
    session = 8
    lap = 9
    course_point = 10
    battery = 11
    virtual_partner_pace = 12
    hr_high_alert = 13
    hr_low_alert = 14
    speed_high_alert = 15
    speed_low_alert = 16
    cad_high_alert = 17
    cad_low_alert = 18
    power_high_alert = 19
    power_low_alert = 20
    recovery_hr = 21
    battery_low = 22
    time_duration_alert = 23
    distance_duration_alert = 24
    calorie_duration_alert = 25
    activity = 26
    fitness_equipment = 27
    length = 28
    user_marker = 32
    sport_point = 33
    calibration = 36
    unknown = 41
    front_gear_change = 42
    rear_gear_change = 43
    rider_position_change = 44
    elev_high_alert = 45
    elev_low_alert = 46
    comm_timeout = 47
    sleep = 74
    radar_threat_alert = 75


class EventType(FieldEnum):
    start = 0
    stop = 1
    consecutive_depreciated = 2
    marker = 3
    stop_all = 4
    begin_depreciated = 5
    end_depreciated = 6
    end_all_depreciated = 7
    stop_disable = 8
    stop_disable_all = 9


class LapTrigger(FieldEnum):
    manual = 0
    time = 1
    distance = 2
    position_start = 4
    position_waypoint = 5
    position_marked = 6
    session_end = 7
    fitness_equipment = 8


class SessionTrigger(FieldEnum):
    activity_end = 0
    manual = 1
    auto_multi_sport = 2
    fitness_equipment = 3


class PersonalRecordType(FieldEnum):
    time        = 0
    distance    = 1
    elevation   = 2
    power       = 3


class GoalType(FieldEnum):
    time            = 0
    distance        = 1
    calories        = 2
    frequency       = 3
    steps           = 4
    ascent          = 5
    active_minutes  = 6


class GoalRecurrence(FieldEnum):
    off             = 0
    daily           = 1
    weekly          = 2
    monthly         = 3
    yearly          = 4
    custom          = 5


class GoalSource(FieldEnum):
    auto            = 0
    community       = 1
    user            = 2


class WatchFaceMode(FieldEnum):
    """A enum that describes a mode of the watch face."""

    digital         = 0
    analog          = 1
    connect_iq      = 2
    disabled        = 3


class ClimbProEvent(FieldEnum):
    """A enum that contains an event from a climbing program."""

    approach        = 0
    start           = 1
    complete        = 2


class HeartRateZonesTimerType(FieldEnum):
    """Gives the type of the Heart Rate Zone Timer."""

    session = 18
    lap = 19


class HeartRateZonesMethod(FieldEnum):
    """Gives the method used to calculate the heart rate zones."""

    custom = 0
    max_heart_rate = 1
    heart_rate_reserve = 2
    lactate_threshhold = 3


class SleepActivityLevel(FieldEnum):
    """Enum of values used to encode activity levels during sleep."""

    unknown = 0
    awake = 1.0
    light_sleep = 2.0
    deep_sleep = 3.0
    rem_sleep = 4.0
