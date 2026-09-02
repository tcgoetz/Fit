"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from .enum import Enum


class Event(Enum):
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


class EventType(Enum):
    """An enum representing a FIT event type field value."""

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
