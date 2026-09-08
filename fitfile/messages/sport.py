"""Structured data for decoding a FIT file sport message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import StringField, SportField, SubSportField, SwitchField


sport_message = {
    0 : SportField(),
    1 : SubSportField(),
    3 : StringField('name'),
    #
    15 : SwitchField('popularity_routing'),
    18 : SwitchField('sharp_bend_warnings'),
    21 : SwitchField('workout_videos'),
    22 : SwitchField('high_traffic_road_warnings'),
    23 : SwitchField('road_hazard_warnings'),
    24 : SwitchField('unpaved_road_warnings'),
}
