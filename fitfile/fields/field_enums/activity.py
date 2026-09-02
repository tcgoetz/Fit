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


class Sport(Enum):
    """Enums that represent FIT file message sport field values."""

    generic                 = 0
    running                 = 1
    cycling                 = 2
    transition              = 3
    fitness_equipment       = 4
    swimming                = 5
    basketball              = 6
    soccer                  = 7
    tennis                  = 8
    american_football       = 9
    training                = 10
    walking                 = 11
    cross_country_skiing    = 12
    alpine_skiing           = 13
    snowboarding            = 14
    rowing                  = 15
    mountaineering          = 16
    hiking                  = 17
    multisport              = 18
    paddling                = 19
    flying                  = 20
    e_biking                = 21
    motorcycling            = 22
    boating                 = 23
    driving                 = 24
    golf                    = 25
    hang_gliding            = 26
    horseback_riding        = 27
    hunting                 = 28
    fishing                 = 29
    inline_skating          = 30
    rock_climbing           = 31
    sailing                 = 32
    ice_skating             = 33
    sky_diving              = 34
    snowshoeing             = 35
    snowmobiling            = 36
    stand_up_paddleboarding = 37
    surfing                 = 38
    wakeboarding            = 39
    water_skiing            = 40
    kayaking                = 41
    rafting                 = 42
    windsurfing             = 43
    kitesurfing             = 44
    tactical                = 45
    jumpmaster              = 46
    boxing                  = 47
    floor_climbing          = 48
    baseball                = 49
    diving                  = 53
    emergency_alert         = 54  # Not documented in the SDK, could mean something else
    #
    shooting                = 56
    #
    winter_sport            = 58
    grinding                = 59
    #
    hiit                    = 62
    video_gaming            = 63
    racket                  = 64
    wheelchair_push_walk    = 65
    wheelchair_push_run     = 66
    meditation              = 67
    para_sport              = 68
    disc_golf               = 69
    team_sport              = 70
    cricket                 = 71
    rugby                   = 72
    hockey                  = 73
    lacrosse                = 74
    volleyball              = 75
    water_tubing            = 76
    wakesurfing             = 77
    water_sport             = 78
    archery                 = 79
    mixed_martial_arts      = 80
    motor_sports            = 81
    snorkeling              = 82
    dance                   = 83
    jump_rope               = 84
    pool_apnea              = 85
    mobility                = 86
    geocaching              = 87
    canoeing                = 88
    all                     = 254
    invalid                 = 255

    def preferred(self):
        """Return if this Sport enum instance is a preferred value or not."""
        return self.value > Sport.generic.value and self.value < Sport.all.value

    def activity_name(self):
        activity_name_str = {
            'running': 'run',
            'cycling': 'ride',
            'walking': 'walk',
            'hiking': 'hike',
            'swimming': 'swim',
            'paddling': 'paddle',
            'kayaking': 'kayak'
        }
        return activity_name_str[self.name] if self.name in activity_name_str else self.name


class SubSport(Enum):
    """An enum field containing more specific sport information."""

    generic                 = 0
    treadmill               = 1
    street                  = 2
    trail                   = 3
    track                   = 4
    spin                    = 5
    indoor_cycling          = 6
    road                    = 7
    mountain                = 8
    downhill                = 9
    recumbent               = 10
    cyclocross              = 11
    hand_cycling            = 12
    track_cycling           = 13
    indoor_rowing           = 14
    elliptical              = 15
    stair_climbing          = 16
    lap_swimming            = 17
    open_water              = 18
    flexibility_training    = 19
    strength_training       = 20
    warm_up                 = 21
    match                   = 22
    exercise                = 23
    challenge               = 24
    indoor_skiing           = 25
    cardio_training         = 26
    indoor_walking          = 27
    e_bike_fitness          = 28
    bmx                     = 29
    casual_walking          = 30
    speed_walking           = 31
    bike_to_run_transition  = 32
    run_to_bike_transition  = 33
    swim_to_bike_transition = 34
    atv                     = 35
    motocross               = 36
    backcountry             = 37
    resort                  = 38
    rc_drone                = 39
    wingsuit                = 40
    whitewater              = 41
    skate_skiing            = 42
    yoga                    = 43
    pilates                 = 44
    indoor_running          = 45
    gravel_cycling          = 46
    e_bike_mountain         = 47
    commuting               = 48
    mixed_surface           = 49
    navigate                = 50
    track_me                = 51
    map                     = 52
    single_gas_diving       = 53
    multi_gas_diving        = 54
    guage_diving            = 55
    apnea_diving            = 56
    apneas_hunting          = 57
    virtual_activity        = 58
    obstacle                = 59
    #
    breathing               = 62
    ccr_diving              = 63
    #
    sail_race               = 65
    expedition              = 66
    ultra                   = 67
    indoor_climbing         = 68
    bouldering              = 69
    hiit                    = 70
    indoor_grinding         = 71
    hunting_with_dogs       = 72
    amrap                   = 73
    emom                    = 74
    tabata                  = 75
    #
    esport                  = 77
    triathlon               = 78
    duathlon                = 79
    brick                   = 80
    swim_run                = 81
    adventure_race          = 82
    dance                   = 83
    pickleball              = 84
    padel                   = 85
    indoor_wheelchair_walk  = 86
    indoor_wheelchair_run   = 87
    indoor_hand_cycling     = 88
    #
    field                   = 90
    ice                     = 91
    ultimate                = 92
    platform                = 93
    squash                  = 94
    badminton               = 95
    racquetball             = 96
    table_tennis            = 97
    overland                = 98
    trolling_motor          = 99
    #
    fly_canopy              = 110
    fly_paraglide           = 111
    fly_paramotor           = 112
    fly_pressurized         = 113
    fly_navigate            = 114
    fly_altimeter           = 116
    fly_wx                  = 117
    fly_vfr                 = 118
    fly_ifr                 = 119
    #
    dynamic_apnea           = 121
    #
    enduro                  = 123
    rucking                 = 124
    rally                   = 125
    pool_triathlon          = 126
    e_bike_enduro           = 127
    #
    all                     = 254
    invalid                 = 255

    def preferred(self):
        """Return if this SubSport enum instance is a preferred value or not."""
        return self.value > SubSport.generic.value and self.value < SubSport.all.value


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


class AutoPauseSetting(Enum):
    off = 0
    when_stopped = 1
    custom = 2


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


class AutoScrollMode(Enum):
    off = 0
    slow = 1
    medium = 2
    fast = 3
