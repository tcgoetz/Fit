"""Objects defining FIT file message types."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


import enum

from .exceptions import FitMessageType


class UnknownMessageType():
    """Represents an unknown FIT file message type."""

    def __init__(self, index):
        """Return an instance of UnknownMessageType."""
        self.value = index
        self.name = 'unknown_%d' % index

    def __eq__(self, other):
        return other and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self.value

    def __repr__(self):
        """Return a string representation of the UnknownMessageType instance."""
        return f'<UnknownMessageType.{self.name}: {self.value}>'


#
# Some undocumented values from https://medium.com/@harry_90407/beyond-the-fit-sdk-c9969430aeeb
#

class MessageType(enum.Enum):
    """Enum of all known FIT file message types."""

    file_id                                 = 0
    capabilities                            = 1
    device_settings                         = 2
    user_profile                            = 3
    hrm_profile                             = 4
    sdm_profile                             = 5
    bike_profile                            = 6
    zones_target                            = 7
    hr_zone                                 = 8
    power_zone                              = 9
    met_zone                                = 10
    # 11 is unknown
    sport                                   = 12
    training_settings                       = 13
    data_screen                             = 14
    goal                                    = 15
    alert                                   = 16
    range_alert                             = 17
    session                                 = 18
    lap                                     = 19
    record                                  = 20
    event                                   = 21
    device_used                             = 22
    device_info                             = 23
    # 24,25 are unknown
    unknown_24                              = 24
    workout                                 = 26
    workout_step                            = 27
    schedule                                = 28
    location                                = 29
    weight_scale                            = 30
    course                                  = 31
    course_point                            = 32
    totals                                  = 33
    activity                                = 34
    software                                = 35
    # 36 not known
    file_capabilities                       = 37
    mesg_capabilities                       = 38
    field_capabilities                      = 39
    # 40-48 not known
    file_creator                            = 49
    blood_pressure                          = 51
    # 52 not known
    speed_zone                              = 53
    # 54 not known
    monitoring                              = 55
    # 56-69 not known
    map_layer                               = 70
    routing                                 = 71
    training_file                           = 72
    # 73-77 not known
    hrv                                     = 78
    user_metrics                            = 79
    ant_rx                                  = 80
    ant_tx                                  = 81
    ant_channel_id                          = 82
    # 83-100 not known
    open_water_event                        = 89
    length                                  = 101
    # 102 not known
    monitoring_info                         = 103
    device_status                           = 104
    pad                                     = 105
    slave_device                            = 106
    best_effort                             = 113
    personal_record                         = 114
    # 107-126 not known
    connectivity                            = 127
    weather_conditions                      = 128
    weather_alert                           = 129
    # 130 not known
    cadence_zone                            = 131
    hr                                      = 132
    # 133-139 not known
    activity_metrics                        = 140
    epo_status                              = 141
    segment_lap                             = 142
    multisport_settings                     = 143
    multisport_activity                     = 144
    memo_glob                               = 145
    # 146 not known
    sensor                                  = 147
    segment_id                              = 148
    segment_leaderboard_entry               = 149
    segment_point                           = 150
    segment_file                            = 151
    metronome                               = 152
    # 153-157 not known
    workout_session                         = 158
    watchface_settings                      = 159
    gps_metadata                            = 160
    camera_event                            = 161
    timestamp_correlation                   = 162
    # 163 not known
    gyroscope_data                          = 164
    accelerometer_data                      = 165
    # 166 not known
    three_d_sensor_calibration              = 167
    # 168 not known
    video_frame                             = 169
    connect_iq_field                        = 170
    # 171-172 not known
    clubs                                   = 173
    obdii_data                              = 174
    # 175,176 not known
    nmea_sentence                           = 177
    aviation_attitude                       = 178
    # 179-183 not known
    video                                   = 184
    video_title                             = 185
    video_description                       = 186
    video_clip                              = 187
    ohr_settings                            = 188
    waypoint_handling                       = 189
    golf_course                             = 190
    golf_stats                              = 191
    score                                   = 192
    hole                                    = 193
    shot                                    = 194
    # 195-199 not known
    exd_screen_configuration                = 200
    exd_data_field_configuration            = 201
    exd_data_concept_configuration          = 202
    # 203-205 not known
    field_description                       = 206
    dev_data_id                             = 207
    magnetometer_data                       = 208
    barometer_data                          = 209
    one_d_sensor_calibration                = 210
    monitoring_hr_data                      = 211
    # 212-215 not known
    time_in_zone                            = 216
    # 217-224 not known
    alarm_settings                          = 222
    set                                     = 225
    # 226 not known
    stress_level                            = 227
    max_met_data                            = 229
    # 229-241 not known
    metrics_232                             = 232  # guess, file type metrics
    unknown_233                             = 233
    local_time                              = 241
    music_info                              = 243
    # 242-257 not known
    dive_settings                           = 258
    dive_gas                                = 259
    # 260,261 not known
    dive_alarm                              = 262
    # 263 not known
    exercise_title                          = 264
    # 265-267 not known
    dive_summary                            = 268
    pulse_ox                                = 269
    sleep_data_info                         = 273
    sleep_data                              = 274  # this is a guess
    sleep_level                             = 275
    end                                     = 276  # this is a guess
    metrics_281                             = 281  # guess, file type metrics
    metrics_282                             = 282  # guess, file type metrics
    unknown_284                             = 284
    jump                                    = 285
    respiration_rate                        = 297
    aad_accel_features                      = 289
    beat_intervals                          = 290
    metrics_294                             = 294  # guess, file type metrics
    hsa_accelerometer_data                  = 302
    hsa_step_data                           = 304
    hsa_spo2_data                           = 305
    hsa_spo2_data2                          = 306
    hsa_respiration_data                    = 307
    hsa_heart_rate_data                     = 308
    mtb_cx                                  = 309
    race                                    = 310
    split_time                              = 311
    split                                   = 312
    split_summary                           = 313
    hsa_body_battery_data                   = 314
    hsa_event                               = 315
    #
    climb_pro                               = 317
    tank_update                             = 319
    power_mode                              = 321
    tank_summary                            = 323
    gps_event                               = 326
    ecg_summary                             = 336
    ecg_raw_sample                          = 337
    ecg_smooth_sample                       = 338
    sleep_assessment                        = 346
    functional_metrics                      = 356
    race_event                              = 358
    #
    training_readiness                      = 369
    hrv_status_summary                      = 370
    hrv_value                               = 371
    raw_bbi                                 = 372
    device_aux_battery_info                 = 375
    hsa_gyroscope_data                      = 376
    training_load                           = 378
    sleep_schedule                          = 379
    sleep_restless_moments                  = 382
    chrono_shot_session                     = 387
    chrono_shot_data                        = 388
    hsa_configuration_data                  = 389
    dive_apnea_alarm                        = 393
    cpe_status                              = 394
    skin_temp                               = 397
    skin_temp_overnight                     = 398
    hill_score                              = 402
    endurance_score                         = 403
    hsa_wrist_temperature_data              = 409
    nap_event                               = 412
    workout_schedule                        = 428
    sleep_disruption_severity_period        = 470
    sleep_disruption_overnight_severity     = 471
    #
    metrics_493                             = 493
    #
    mfg_range_min                           = 0xFF00
    mfg_range_max                           = 0xFFFE

    def is_unknown(self):
        """Return if the message type is not a known type."""
        return "unknown" in self.name

    @classmethod
    def get_type(cls, message_number):
        """Given a message number, return the message type."""
        if message_number < 0 or message_number > cls.mfg_range_max.value:
            raise FitMessageType(f'Message number {message_number} out of range')
        try:
            return cls(message_number)
        except ValueError:
            return UnknownMessageType(message_number)
