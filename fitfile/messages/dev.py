"""Structured data for decoding a FIT file message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, IntegerField, FitBaseTypeField, StringField, FloatField, FitBaseUnitField, BytesField, ManufacturerField


field_description_message = {
    0 : IntegerField('developer_data_index'),
    1 : NamedField('field_definition_number'),
    2 : FitBaseTypeField('fit_base_type_id'),
    3 : StringField('field_name'),
    4 : NamedField('array'),
    5 : StringField('components'),
    6 : FloatField('scale'),
    7 : FloatField('offset'),
    8 : StringField('units'),
    9 : StringField('bits'),
    10 : StringField('accumulate'),
    13 : FitBaseUnitField('fit_base_unit_id'),
    14 : IntegerField('native_message_num'),
    15 : IntegerField('native_field_num')
}


dev_data_id_message = {
    0 : NamedField('developer_id'),
    1 : BytesField('application_id'),
    2 : ManufacturerField(),
    3 : IntegerField('developer_data_index'),
    4 : NamedField('application_version')
}
