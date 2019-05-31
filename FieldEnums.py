#!/usr/bin/env python

#
# copyright Tom Goetz
#


import enum


def name_for_enum(enum_instance):
    if enum_instance is not None:
        name = getattr(enum_instance, 'name', None)
        if name:
            return name
        else:
            return enum_instance


class UnknownEnumValue(object):
    def __init__(self, type, index):
        self.type = type
        self.value = index
        self.name = '%s_%d' % (type, index)

    def __eq__(self, other):
        return other and (isinstance(other, UnknownEnumValue) and self.value == other.value) or (not isinstance(other, UnknownEnumValue) and self.value == other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.value

    def __repr__(self):
        return '<%s.%s: %d>' % (self.type, self.name, self.value)


class FieldEnum(enum.Enum):
    @classmethod
    def from_string_ext(cls, string):
        for name, value in cls.__members__.items():
            if name in string:
                return value

    @classmethod
    def from_string(cls, string):
        try:
            try:
                return cls(string)
            except:
                return getattr(cls, string)
        except AttributeError:
            return cls.from_string_ext(string)


class Switch(enum.Enum):
    off         = 0
    on          = 1
    auto        = 2
    invalid     = 255


class FitBaseUnit(enum.Enum):
    other       = 0
    kg          = 1
    lb          = 2
    invalid     = 255


class DisplayMeasure(FieldEnum):
    metric      = 0
    statute     = 1
    nautical    = 2
    invalid     = 255


class DisplayHeart(enum.Enum):
    bpm     = 0
    max     = 1
    reserve = 2
    invalid = 255


class DisplayPosition(enum.Enum):
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


class Manufacturer(FieldEnum):
    #
    # Garmin defined values
    #
    Garmin                          = 1
    garmin_fr405_antfs              = 2
    zephyr                          = 3
    dayton                          = 4
    idt                             = 5
    srm                             = 6
    quarq                           = 7
    ibike                           = 8
    saris                           = 9
    spark_hk                        = 10
    tanita                          = 11
    echowell                        = 12
    Dynastream_OEM                  = 13
    nautilus                        = 14
    Dynastream                      = 15
    timex                           = 16
    metrigear                       = 17
    xelic                           = 18
    beurer                          = 19
    cardiosport                     = 20
    a_and_d                         = 21
    hmm                             = 22
    Suunto                          = 23
    thita_elektronik                = 24
    gpulse                          = 25
    clean_mobile                    = 26
    pedal_brain                     = 27
    peaksware                       = 28
    saxonar                         = 29
    lemond_fitness                  = 30
    dexcom                          = 31
    Wahoo_Fitness                   = 32
    Octane_Fitness                  = 33
    archinoetics                    = 34
    the_hurt_box                    = 35
    citizen_systems                 = 36
    magellan                        = 37
    osynce                          = 38
    holux                           = 39
    concept2                        = 40
    one_giant_leap                  = 42
    ace_sensor                      = 43
    brim_brothers                   = 44
    xplova                          = 45
    perception_digital              = 46
    bf1systems                      = 47
    pioneer                         = 48
    spantec                         = 49
    metalogics                      = 50
    _4iiiis                         = 51
    seiko_epson                     = 52
    seiko_epson_oem                 = 53
    ifor_powell                     = 54
    maxwell_guider                  = 55
    Star_Trac                       = 56
    breakaway                       = 57
    alatech_technology_ltd          = 58
    mio_technology_europe           = 59
    rotor                           = 60
    geonaute                        = 61
    id_bike                         = 62
    Specialized                     = 63
    wtek                            = 64
    physical_enterprises            = 65
    north_pole_engineering          = 66
    bkool                           = 67
    cateye                          = 68
    stages_cycling                  = 69
    sigmasport                      = 70
    TomTom                          = 71
    peripedal                       = 72
    wattbike                        = 73
    moxy                            = 76
    ciclosport                      = 77
    powerbahn                       = 78
    acorn_projects_aps              = 79
    lifebeam                        = 80
    Bontrager                       = 81
    wellgo                          = 82
    Scosche                         = 83
    magura                          = 84
    woodway                         = 85
    elite                           = 86
    nielsen_kellerman               = 87
    dk_city                         = 88
    tacx                            = 89
    direction_technology            = 90
    magtonic                        = 91
    OnePartCarbon                   = 92
    inside_ride_technologies        = 93
    sound_of_motion                 = 94
    stryd                           = 95
    icg                             = 96
    MiPulse                         = 97
    bsx_athletics                   = 98
    look                            = 99
    campagnolo_srl                  = 100
    body_bike_smart                 = 101
    praxisworks                     = 102
    limits_technology               = 103
    topaction_technology            = 104
    cosinuss                        = 105
    fitcare                         = 106
    magene                          = 107
    giant_manufacturing_co          = 108
    tigrasport                      = 109
    salutron                        = 110
    TechnoGym                       = 111
    Bryton_Sensors                  = 112
    Latitude_Limited                = 113
    Soaring_Technology              = 114
    IGPSport                        = 115
    ThinkRider                      = 116
    GopherSport                     = 117
    WaterPower                      = 118
    OrangeTheory                    = 119
    Inpeak                          = 120
    Kinetic                         = 121
    Johnson_Health_Tech             = 122
    Polar_Electro                   = 123
    Seesense                        = 124
    development                     = 255
    healthandlife                   = 257
    lezyne                          = 258
    scribe_labs                     = 259
    zwift                           = 260
    watteam                         = 261
    recon                           = 262
    favero_electronics              = 263
    dynovelo                        = 264
    Strava                          = 265
    precor                          = 266
    bryton                          = 267
    sram                            = 268
    navman                          = 269
    cobi                            = 270
    spivi                           = 271
    mio_magellan                    = 272
    evesports                       = 273
    sensitivus_gauge                = 274
    podoon                          = 275
    Life_Time_Fitness               = 276
    falco_e_motors                  = 277
    Minoura                         = 278
    Cycliq                          = 279
    Luxottica                       = 280
    Trainer_Road                    = 281
    The_Sufferest                   = 282
    FullSpeedAhead                  = 283
    VirtualTraining                 = 284
    FeedbackSports                  = 285
    Omata                           = 286
    VDO                             = 287
    MagneticDays                    = 288
    Hammerhead                      = 289
    Kinetic_By_Kurt                 = 290
    Shapelog                        = 291
    Dabuziduo                       = 292
    JetBlack                        = 293
    Coros                           = 294
    virtugo                         = 295
    velosense                       = 296
    cycligentinc                    = 297
    trailforks                      = 298
    actigraphcorp                   = 5759
    #
    # Privates values
    #
    Garmin_local_0                  = 0
    Garmin_local_14738              = 14738
    Garmin_local_22208              = 22208
    Garmin_local_31533              = 31533
    Garmin_local_34213              = 34213
    Garmin_local_42664              = 42664
    Garmin_local_42768              = 42768
    Garmin_local_43064              = 43064
    Garmin_local_43168              = 43168
    Garmin_local_43304              = 43304
    Garmin_local_45192              = 45192
    Garmin_local_45528              = 45528
    Garmin_local_47656              = 47656
    Garmin_local_45712              = 45712
    Garmin_local_45784              = 45784
    Garmin_local_52416              = 52416
    Garmin_local_61440              = 61440
    Garmin_local_65533              = 65533
    invalid                         = 65535


class GarminProduct(FieldEnum):
    Bluetooth_Low_Energy_Chipset    = 0
    HRM1                            = 1
    axh01                           = 2
    axb01                           = 3
    axb02                           = 4
    hrm2ss                          = 5
    dsi_alf02                       = 6
    hrm3ss                          = 7
    hrm_run_single_byte_product_id  = 8
    Bike_Speed_Sensor               = 9
    Bike_Cadence_Sensor             = 10
    axs01                           = 11
    hrm_tri_single_byte_product_id  = 12
    fr225_single_byte_product_id    = 14
    fr301_china                     = 473
    fr301_japan                     = 474
    fr301_korea                     = 475
    fr301_taiwan                    = 494
    fr405                           = 717
    fr50                            = 782
    fr405_japan                     = 987
    fr60                            = 988
    dsi_alf01                       = 1011
    fr310xt                         = 1018
    edge500                         = 1036
    fr110                           = 1124
    edge800                         = 1169
    edge500_taiwan                  = 1199
    edge500_japan                   = 1213
    chirp                           = 1253
    fr110_japan                     = 1274
    edge200                         = 1325
    fr910xt                         = 1328
    edge800_taiwan                  = 1333
    edge800_japan                   = 1334
    alf04                           = 1341
    fr610                           = 1345
    fr210_japan                     = 1360
    vector_ss                       = 1380
    vector_cp                       = 1381
    edge800_china                   = 1386
    edge500_china                   = 1387
    fr610_japan                     = 1410
    edge500_korea                   = 1422
    fr70                            = 1436
    fr310xt_4t                      = 1446
    amx                             = 1461
    fr10                            = 1482
    edge800_korea                   = 1497
    swim                            = 1499
    fr910xt_china                   = 1537
    Fenix                           = 1551
    edge200_taiwan                  = 1555
    edge510                         = 1561
    edge810                         = 1567
    Tempe                           = 1570
    fr910xt_japan                   = 1600
    GPS_1620                        = 1620
    GPS_1621                        = 1621
    fr620                           = 1623
    fr220                           = 1632
    fr910xt_korea                   = 1664
    fr10_japan                      = 1688
    edge810_japan                   = 1721
    virb_elite                      = 1735
    edge_touring                    = 1736
    edge510_japan                   = 1742
    HRM_Tri                         = 1743
    HRM_Run                         = 1752
    fr920xt                         = 1765
    edge510_asia                    = 1821
    edge810_china                   = 1822
    edge810_taiwan                  = 1823
    edge1000                        = 1836
    vivofit                         = 1837
    virb_remote                     = 1853
    vivo_ki                         = 1885
    fr15                            = 1903
    VivoActive                      = 1907
    edge510_korea                   = 1918
    fr620_japan                     = 1928
    fr620_china                     = 1929
    fr220_japan                     = 1930
    fr220_china                     = 1931
    approach_s6                     = 1936
    VivoSmart                       = 1956
    Fenix2                          = 1967
    epix                            = 1988
    Fenix3                          = 2050
    edge1000_taiwan                 = 2052
    edge1000_japan                  = 2053
    fr15_japan                      = 2061
    edge520                         = 2067
    edge1000_china                  = 2070
    fr620_russia                    = 2072
    fr220_russia                    = 2073
    vector_s                        = 2079
    edge1000_korea                  = 2100
    fr920xt_taiwan                  = 2130
    fr920xt_china                   = 2131
    fr920xt_japan                   = 2132
    virbx                           = 2134
    vivo_smart_apac                 = 2135
    etrex_touch                     = 2140
    edge25                          = 2147
    fr25                            = 2148
    VivoFit2                        = 2150
    fr225                           = 2153
    fr630                           = 2156
    fr230                           = 2157
    vivo_active_apac                = 2160
    vector_2                        = 2161
    vector_2s                       = 2162
    virbxe                          = 2172
    fr620_taiwan                    = 2173
    fr220_taiwan                    = 2174
    truswing                        = 2175
    Fenix3_china                    = 2188
    Fenix3_twn                      = 2189
    varia_headlight                 = 2192
    varia_taillight_old             = 2193
    edge_explore_1000               = 2204
    fr225_asia                      = 2219
    varia_radar_taillight           = 2225
    varia_radar_display             = 2226
    edge20                          = 2238
    D2_Bravo                        = 2262
    approach_s20                    = 2266
    varia_remote                    = 2276
    HRM4_Run                        = 2327
    VivoActive_HR                   = 2337
    VivoSmart_GPS_HR                = 2347
    VivoSmart_HR                    = 2348
    VivoMove                        = 2368
    varia_vision                    = 2398
    VivoFit3                        = 2406
    Fenix3_HR                       = 2413
    Index_Smart_Scale               = 2429
    fr235                           = 2431
    Fenix3_Chronos                  = 2432
    oregon7xx                       = 2441
    Rino_7xx                        = 2444
    nautix                          = 2496
    Forerunner35                    = 2503
    Edge_820                        = 2530
    Edge_Explore_820                = 2531
    Fenix5s                         = 2544
    D2_Bravo_Titanium               = 2547
    Varia_UT800                     = 2567
    Running_Dynamics_Pod            = 2593
    Fenix5X                         = 2604
    VivoFit_Jr                      = 2606
    VivoSport                       = 2623
    Forerunner935                   = 2691
    Fenix5_Sapphire                 = 2697
    VivoActive_3                    = 2700
    Edge_1030                       = 2713
    VivoMove_HR                     = 2772
    Approach_z80                    = 2806
    VivoSmart3_Apac                 = 2831
    VivoSport_Apac                  = 2832
    Descent                         = 2859
    fr645                           = 2886
    fr645m                          = 2888
    Fenix5s_Plus                    = 2900
    Edge_130                        = 2909
    Vivosmart_4                     = 2927
    Approach_x10                    = 2962
    VivoActive_3m_w                 = 2988
    Edge_Explore                    = 3011
    GPSMap66                        = 3028
    Approach_S10                    = 3049
    VivoActive_3M_l                 = 3066
    Approach_G80                    = 3085
    Fenix5_plus                     = 3110
    Fenix5x_plus                    = 3111
    Edge_520_plus                   = 3112
    Approach_S40                    = 3314
    HRM_Dual                        = 3299
    Accelerometer_8194              = 8194
    FootPod_SDM4                    = 10007
    Accelerometer                   = 17530
    edge_remote                     = 10014
    Training_Center                 = 20119
    Accelerometer_21909             = 21909
    BTLE_Chipset                    = 24832
    Connectiq_Simulator             = 65531
    Android_Antplus_plugin          = 65532
    connect                         = 65534
    #
    # Privates values
    #
    Fenix5_Sapphire_local_8195      = 8195


class WahooFitnessProduct(FieldEnum):
    RPM_Sensor                      = 6


class ScoscheProduct(FieldEnum):
    Rhythm_Plus_Armband_HRM         = 2


class UnknownProduct(UnknownEnumValue):
    def __init__(self, index):
        UnknownEnumValue.__init__(self, 'UnknownProduct', index)


def product_enum(manufacturer, product_str):
    _manufacturer_to_product_enum = {
        Manufacturer.Garmin                 : GarminProduct,
        Manufacturer.Dynastream             : GarminProduct,
        Manufacturer.Dynastream_OEM         : GarminProduct,
        Manufacturer.Scosche                : ScoscheProduct,
        Manufacturer.Wahoo_Fitness          : WahooFitnessProduct,
        Manufacturer.Garmin_local_0         : GarminProduct,
        Manufacturer.Garmin_local_14738     : GarminProduct,
        Manufacturer.Garmin_local_22208     : GarminProduct,
        Manufacturer.Garmin_local_31533     : GarminProduct,
        Manufacturer.Garmin_local_42664     : GarminProduct,
        Manufacturer.Garmin_local_42768     : GarminProduct,
        Manufacturer.Garmin_local_43064     : GarminProduct,
        Manufacturer.Garmin_local_43168     : GarminProduct,
        Manufacturer.Garmin_local_43304     : GarminProduct,
        Manufacturer.Garmin_local_45192     : GarminProduct,
        Manufacturer.Garmin_local_47656     : GarminProduct,
        Manufacturer.Garmin_local_45784     : GarminProduct,
        Manufacturer.Garmin_local_45712     : GarminProduct,
        Manufacturer.Garmin_local_52416     : GarminProduct,
        Manufacturer.Garmin_local_61440     : GarminProduct,
        Manufacturer.Garmin_local_65533     : GarminProduct,
        Manufacturer.invalid                : GarminProduct,
    }
    return _manufacturer_to_product_enum[manufacturer].from_string(product_str)


class DisplayOrientation(enum.Enum):
    auto = 0
    portrait = 1
    landscape = 2
    portrait_flipped = 3
    landscape_flipped = 4
    invalid = 255


class Side(enum.Enum):
    right = 0
    left = 1
    invalid = 255


class BacklightMode(enum.Enum):
    off = 0
    manual = 1
    key_and_messages = 2
    auto_brightness = 3
    smart_notifications = 4
    key_and_messages_night = 5
    key_and_messages_and_smart_notifications = 6
    invalid = 255


class AntNetwork(enum.Enum):
    public  = 0
    antplus = 1
    antfs   = 2
    invalid = 255


class SourceType(enum.Enum):
    ant = 0
    antplus = 1
    bluetooth = 2
    bluetooth_low_energy = 3
    wifi = 4
    local = 5
    invalid = 255


class AntplusDeviceType(enum.Enum):
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

class LocalDeviceType(enum.Enum):
    gps                             = 0
    accelerometer                   = 3
    barometer                       = 4
    bluetooth_low_energy_chipset    = 8
    wrist_heart_rate                = 10



class UnknownDeviceType(UnknownEnumValue):
    def __init__(self, index):
        UnknownEnumValue.__init__(self, 'UnknownDeviceType', index)


class BatteryStatus(enum.Enum):
    new = 1
    good = 2
    ok = 3
    low = 4
    critical = 5
    charging = 6
    unknown = 7
    invalid = 255


class AutoSyncFrequency(enum.Enum):
    never = 0
    occasionally = 1
    frequent = 2
    once_a_day = 3
    remote = 4
    invalid = 255


class BodyLocation(enum.Enum):
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


class Gender(enum.Enum):
    female = 0
    male = 1


class HeartRateZoneCalc(enum.Enum):
    custom = 0
    percent_max_hr = 1
    percent_hrr = 2
    invalid = 255


class PowerCalc(enum.Enum):
    custom = 0
    percent_ftp = 1
    invalid = 255


class Language(enum.Enum):
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


class DateMode(enum.Enum):
    day_month   = 0
    month_day   = 1
    invalid     = 255


class TimeMode(enum.Enum):
    twelve_hour             = 0
    twentyfour_hour         = 1
    military                = 2
    twelve_hour_secs        = 3
    twentyfour_hour_secs    = 4
    utc                     = 5
    invalid                 = 255


class Activity(enum.Enum):
    manual              = 0
    auto_multi_sport    = 1


class ActivityType(enum.Enum):
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


class FileType(enum.Enum):
    #
    # Garmin defined values
    #
    unknown0                    = 0
    device                      = 1
    settings                    = 2
    sport_settings              = 3
    activity                    = 4
    workout                     = 5
    course                      = 6
    schedules                   = 7
    weight                      = 9
    totals                      = 10
    goals                       = 11
    blood_pressure              = 14
    monitoring_a                = 15
    activity_summary            = 20
    monitoring_daily            = 28
    records                     = 29
    monitoring_b                = 32
    segment                     = 34
    segment_list                = 35
    exd_configuration           = 40
    metrics                     = 44
    sleep                       = 49
    unknown_file_type_64        = 64
    manufacturer_range_start    = 0xfe
    invalid                     = 255


class Event(enum.Enum):
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

class EventType(enum.Enum):
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


class LapTrigger(enum.Enum):
    manual = 0
    time = 1
    distance = 2
    position_start = 4
    position_waypoint = 5
    position_marked = 6
    session_end = 7
    fitness_equipment = 8


class SessionTrigger(enum.Enum):
    activity_end = 0
    manual = 1
    auto_multi_sport = 2
    fitness_equipment = 3


class Sport(enum.Enum):
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
    all                     = 254


class SubSport(enum.Enum):
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
    all                     = 254


class PersonalRecordType(enum.Enum):
    time        = 0
    distance    = 1
    elevation   = 2
    power       = 3

class GoalType(enum.Enum):
    time            = 0
    distance        = 1
    calories        = 2
    frequency       = 3
    steps           = 4
    ascent          = 5
    active_minutes  = 6

class GoalRecurrence(enum.Enum):
    off             = 0
    daily           = 1
    weekly          = 2
    monthly         = 3
    yearly          = 4
    custom          = 5

class GoalSource(enum.Enum):
    auto            = 0
    community       = 1
    user            = 2

class WatchFaceMode(enum.Enum):
    digital         = 0
    analog          = 1
    connect_iq      = 2
    disabled        = 3

