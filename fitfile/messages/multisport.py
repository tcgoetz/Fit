"""Structured data for decoding a FIT file multisport messages."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import StringField, SwitchField, IntegerField, PowerSaveTimeoutField, SportChangeField, SportField, SubSportField


multisport_settings_message = {
    0 : StringField('name'),
    1 : SwitchField('transitions'),
    2 : IntegerField('number_of_activities'),
    3 : SwitchField('auto_pause'),
    4 : SwitchField('alerts'),
    5 : SwitchField('auto_lap'),
    6 : PowerSaveTimeoutField(),
    7 : SwitchField('auto_scroll'),
    8 : SwitchField('repeat'),
    #
    10 : SportChangeField(),
}


multisport_activity_message = {
    0 : SportField(),
    1 : SubSportField(),
    2 : SwitchField('lock_device'),
    3 : StringField('name'),
}
