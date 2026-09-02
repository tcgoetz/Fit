"""Structured data for decoding a FIT file weight scale message."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


from ..fields import NamedField, PercentField, WeightField


weight_scale_message = {
    0 : WeightField('weight'),
    1 : PercentField('percent_fat'),
    2 : PercentField('percent_hydration'),
    3 : WeightField('visceral_fat_mass'),
    4 : WeightField('bone_mass'),
    5 : WeightField('muscle_mass'),
    7 : NamedField('basal_met'),
    8 : NamedField('physique_rating'),
    9 : NamedField('active_met'),
    10 : NamedField('metabolic_age'),
    11 : NamedField('visceral_fat_rating'),
    12 : NamedField('user_profile_index')
}
