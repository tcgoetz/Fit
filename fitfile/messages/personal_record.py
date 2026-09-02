"""Structured data for decoding a FIT file power zone message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import PersonalRecordTypeField, SportField, DistanceCentimetersToMetersField, PersonalRecordField


personal_record_message = {
    0 : PersonalRecordTypeField(),
    1 : SportField(),
    2 : DistanceCentimetersToMetersField('record_distance'),
    3 : DistanceCentimetersToMetersField('record_distance2'),
    4 : DistanceCentimetersToMetersField('actual_distance'),
    5 : PersonalRecordField()
}
