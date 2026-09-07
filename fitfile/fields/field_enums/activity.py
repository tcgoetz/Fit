"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ...enum import Enum


class Activity(Enum):
    manual              = 0
    auto_multi_sport    = 1


class ActivityType(Enum):
    generic             = 0
    running             = 1
    cycling             = 2
    transition          = 3
    fitness_equipment   = 4
    swimming            = 5
    walking             = 6
    sedentary           = 8
    unknown             = 9
    wheelchair_pushing  = 13
    all                 = 245
    invalid             = 255


class LapTrigger(Enum):
    manual = 0
    time = 1
    distance = 2
    position_start = 4
    position_waypoint = 5
    position_marked = 6
    session_end = 7
    fitness_equipment = 8


class AutoLapMode(Enum):
    time = 0
    distance = 1
    position = 2
    manual_only = 6


class PowerCalc(Enum):
    custom      = 0
    percent_ftp = 1
    invalid     = 255


class SessionTrigger(Enum):
    activity_end = 0
    manual = 1
    auto_multi_sport = 2
    fitness_equipment = 3


class PowerZoneCalc(Enum):
    custom = 0
    percent_ftp = 1


class PowerAveraging(Enum):
    include_zeros = 0
    do_not_include_zeros = 1


class Benefit(Enum):	
    no_benefit  = 0
    recovery    = 1
    base        = 2
    tempo       = 3
    threshold   = 4
    vo2_max     = 5
    anaerobic   = 6
    sprint      = 7


class Spo2MeasurementType(Enum):
    off_wrist = 0
    spot_check = 1
    continuous_check = 2
    periodic = 3


class SwimStroke(Enum):
    freestyle       = 0
    backstroke      = 1
    breaststroke    = 2
    butterfly	    = 3
    drill           = 4
    mixed           = 5
    im              = 6
    im_by_round     = 7
    rimo            = 8
    invalid         = 255


class LengthType(Enum):
    idle = 0
    active = 1


class SplitType(Enum):
    ascent_split        = 1
    descent_split       = 2
    interval_active     = 3
    interval_rest       = 4
    interval_warmup     = 5
    interval_cooldown   = 6
    interval_recovery   = 7
    interval_other      = 8
    climb_active        = 9
    climb_rest          = 10
    surf_active         = 11
    run_active          = 12
    run_rest            = 13
    workout_round       = 14
    rwd_run             = 17
    rwd_walk            = 18
    windsurf_active     = 21
    rwd_stand           = 22
    transition          = 23
    ski_lift_split      = 28
    ski_run_split       = 29