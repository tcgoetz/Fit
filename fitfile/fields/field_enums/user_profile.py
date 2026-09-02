"""Objects that represent FIT file object message fields."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

# import idbutils
# from .enum import FuzzyFieldEnum, Enum, CaseInsensitiveFieldEnum
from .enum import Enum, CaseInsensitiveFieldEnum
# from ...measurement import MeasurementSystem


class Gender(CaseInsensitiveFieldEnum):
    female = 0
    male = 1


# DisplayMeasure = idbutils.derived_enum.derive('DisplayMeasure', MeasurementSystem, {})


# class DisplayMeasure(FuzzyFieldEnum):
#     metric      = 0
#     statute     = 1
#     nautical    = 2
#     invalid     = 255


class DisplayHeart(Enum):
    """An enum that defines how heart rate will be displayed."""

    bpm     = 0
    max     = 1
    reserve = 2
    invalid = 255


class DisplayOrientation(Enum):
    auto = 0
    portrait = 1
    landscape = 2
    portrait_flipped = 3
    landscape_flipped = 4
    invalid = 255


class DisplayPosition(Enum):
    """An enum that defines how position data will be displayed."""

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


class Language(Enum):
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