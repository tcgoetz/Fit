#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging, time, datetime

#from time import time, gmtime, localtime, strftime
#from datetime import tzinfo, timedelta, datetime

from FieldValue import FieldValue
from FieldDefinition import FieldDefinition


logger = logging.getLogger(__name__)

class Conversions():
    @classmethod
    def ms_to_dt_time(cls, time_ms):
        if time_ms is not None:
            return (datetime.datetime.min + datetime.timedelta(0, 0, 0, time_ms)).time()
        return None

    @classmethod
    def secs_to_dt_time(cls, time_secs):
        if time_secs is not None:
            return (datetime.datetime.min + datetime.timedelta(0, time_secs)).time()
        return None

    @classmethod
    def min_to_dt_time(cls, time_mins):
        if time_mins is not None:
            return cls.secs_to_dt_time(time_mins * 60)
        return None

    @classmethod
    def meters_to_feet(cls, meters):
        if meters is not None:
            return (meters * 3.2808399)
        return None


class Field():
    attr_units_type_metric = 0
    attr_units_type_english = 1
    attr_units_type_default = attr_units_type_metric

    known_field = True
    _units = [ None, None ]
    _conversion_factor = [ 1, 1 ]
    _conversion_constant = [ 0, 0 ]

    def __init__(self, name=''):
        self.name = name
        if self.__class__.__name__ == 'Field':
            self.type = 'number'
        else:
            self.type = (self.__class__.__name__)[:-len('Field')]
        if not name:
            self.name = self.type
        self._subfield = {}
        self.units_type = self.attr_units_type_default

    def name(self):
        return self._name

    def units(self, value):
        if self._units[self.units_type]:
            return self.convert_many_units(value, None)
        return None

    def sub_field(self, name):
        return _sub_field[name]

    def convert_single(self, value, invalid):
        if value == invalid:
            return None
        return (value / self._conversion_factor[self.units_type]) + self._conversion_constant[self.units_type]

    def _convert_many(self, _convert_single, value, invalid):
        if isinstance(value, list):
            converted_value = []
            for index, sub_value in enumerate(value):
                converted_value.append(_convert_single(value[index], invalid))
        else:
            converted_value = _convert_single(value, invalid)
        return converted_value

    def convert_many(self, value, invalid):
        return self._convert_many(self.convert_single, value, invalid)

    def convert_single_units(self, value, invalid):
        return self._units[self.units_type]

    def convert_many_units(self, value, invalid):
        return self._convert_many(self.convert_single_units, value, invalid)

    def convert(self, value, invalid, english_units=False):
        if english_units:
            self.units_type = Field.attr_units_type_english
        else:
            self.units_type = Field.attr_units_type_metric
        return FieldValue(self, invalid=invalid, value=self.convert_many(value, invalid), orig=value)

    def __repr__(self):
        return self.__class__.__name__ + '(' + self.name + ')'


#
# Special fields
#
class UnknownField(Field):
    known_field = False
    def __init__(self, index):
        Field.__init__(self, "unknown_" + str(index))


class DevField(Field):
    def __init__(self, name, units, scale, offset, *args, **kwargs):
        self._units = [units, units]
        if scale is not None:
            self._conversion_factor = [scale, scale]
        if offset is not None:
            self._conversion_constant = [offset, offset]
        Field.__init__(self, name=name, *args, **kwargs)


#
# Basic field types
#
class BoolField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        try:
            return bool(value)
        except:
            return value


class EnumField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        try:
            return self.enum[value]
        except:
            return value


class SwitchField(EnumField):
    enum = {
        0 : 'off',
        1 : 'on',
        2 : 'auto',
        255 : 'invalid'
    }


class BitField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_single(self, value, invalid):
        return self.bits.get(value, [self.bits[bit] for bit in self.bits if ((bit & value) == bit)])


class LeftRightBalanceField(Field):
    def convert_single(self, value, invalid):
        if value & 0x8000:
            left_or_right = 'Right'
        else:
            left_or_right = 'Left'
        percentage = (value & 0x3fff) / 100
        return left_or_right + ' ' + str(percentage) + '%'


class PercentField(Field):
    _units = [ '%', '%' ]

    def __init__(self, name, scale=1.0, *args, **kwargs):
        self. _conversion_factor = [ 100.0 * scale, 100.0 * scale ]
        Field.__init__(self, name, *args, **kwargs)


class BytePercentField(Field):
    _units = [ '%', '%' ]
    _conversion_factor = [ 2.0, 2.0 ]


class StringField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = ""
            for character in value:
                if character != 0:
                    converted_value += chr(character)
                else:
                    break
        else:
            converted_value = str(value)
        return converted_value.strip()


class BytesField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

    def convert_many(self, value, invalid):
        if isinstance(value, list):
            converted_value = bytearray()
            for character in value:
                converted_value.append(character)
        else:
            converted_value = bytearray(value)
        return converted_value


class DistanceMetersField(Field):
    _units = [ 'm', 'ft' ]
    def __init__(self, name, scale=1.0, *args, **kwargs):
        self._conversion_factor = [ 1.0 * scale, .3048 * scale ]
        Field.__init__(self, name=name, *args, **kwargs)


class EnhancedDistanceMetersField(Field):
    _conversion_factor = [ 1000.0, 304.8 ]
    _units = [ 'm', 'ft' ]


class DistanceCentimetersField(Field):
    _conversion_factor = [ 100000.0, 160934.4 ]
    _units = [ 'km', 'mi' ]


class DistanceMillimetersField(Field):
    _conversion_factor = [ 10.0, 0.3937 ]
    _units = [ 'mm', 'in' ]


#
#
#
class FitBaseUnitField(EnumField):
    enum = {
        0 : 'other',
        1 : 'kg',
        2 : 'lb',
        255 : 'invalid'
    }


class DisplayMeasureField(EnumField):
    enum = {
        0 : 'metric',
        1 : 'statute',
        2 : 'nautical',
        255 : 'invalid'
    }

class DisplayHeartField(EnumField):
    enum = {
        0 : 'bpm',
        1 : 'max',
        2 : 'reserve',
        255 : 'invalid'
    }


class DisplayPositionField(EnumField):
    enum = {
        0 : 'degree',
        1 : 'dregree_minute',
        2 : 'degree_minute_second',
        3 : 'australian_grid',
        4 : 'british_grid',
        5 : 'dutch_grid',
        6 : 'hugarian_grid',
        7 : 'finish_grid',
        8 : 'german_grid',
        9 : 'icelandic_grid',
        10 : 'indonesian_equatorial',
        11 : 'indonesian_irian',
        12 : 'indonesian_southern',
        13 : 'india_zone_0',
        14 : 'india_zone_ia',
        15 : 'india_zone_ib',
        16 : 'india_zone_iia',
        17 : 'india_zone_iib',
        18 : 'india_zone_iiia',
        19 : 'india_zone_iiib',
        20 : 'india_zone_iva',
        21 : 'india_zone_ivb',
        22 : 'irish_traverse',
        23 : 'irish_grid',
        24 : 'loran',
        25 : 'maidenhead_grid',
        26 : 'mgrs_grid',
        27 : 'new_zealand_grid',
        28 : 'new_zealand_traverse',
        29 : 'qatar_grid',
        30 : 'modified_swedish_grid',
        31 : 'swedish_grid',
        32 : 'south_african_grid',
        33 : 'swiss_grid',
        34 : 'tiawan_grid',
        35 : 'united_stated_grid',
        36 : 'utm_ups_grid',
        37 : 'west_malayan',
        38 : 'borneo_rso',
        39 : 'estonian_grid',
        40 : 'latvian_grid',
        41 : 'swedish_ref_99_grid',
        255 : 'invalid'
    }


class FitBaseTypeField(Field):
    def convert_single(self, value, invalid):
        try:
            return FieldDefinition._type_name(value)
        except:
            return value


class MessageNumberField(Field):
    def convert_single(self, value, invalid):
        try:
            #return DefinitionMessageData.get_message_name(value)
            return value
        except:
            return value



#
# Hardware related fields
#
class ManufacturerField(EnumField):
    enum = {
        1 : 'Garmin',
        2 : 'garmin_fr405_antfs',
        3 : 'zephyr',
        4 : 'dayton',
        5 : 'idt',
        6 : 'srm',
        7 : 'quarq',
        8 : 'ibike',
        9 : 'saris',
        10 : 'spark_hk',
        11 : 'tanita',
        12 : 'echowell',
        13 : 'dynastream_oem',
        14 : 'nautilus',
        15 : 'dynastream',
        16 : 'timex',
        17 : 'metrigear',
        18 : 'xelic',
        19 : 'beurer',
        20 : 'cardiosport',
        21 : 'a_and_d',
        22 : 'hmm',
        23 : 'suunto',
        24 : 'thita_elektronik',
        25 : 'gpulse',
        26 : 'clean_mobile',
        27 : 'pedal_brain',
        28 : 'peaksware',
        29 : 'saxonar',
        30 : 'lemond_fitness',
        31 : 'dexcom',
        32 : 'Wahoo Fitness',
        33 : 'octane_fitness',
        34 : 'archinoetics',
        35 : 'the_hurt_box',
        36 : 'citizen_systems',
        37 : 'magellan',
        38 : 'osynce',
        39 : 'holux',
        40 : 'concept2',
        42 : 'one_giant_leap',
        43 : 'ace_sensor',
        44 : 'brim_brothers',
        45 : 'xplova',
        46 : 'perception_digital',
        47 : 'bf1systems',
        48 : 'pioneer',
        49 : 'spantec',
        50 : 'metalogics',
        51 : '4iiiis',
        52 : 'seiko_epson',
        53 : 'seiko_epson_oem',
        54 : 'ifor_powell',
        55 : 'maxwell_guider',
        56 : 'star_trac',
        57 : 'breakaway',
        58 : 'alatech_technology_ltd',
        59 : 'mio_technology_europe',
        60 : 'rotor',
        61 : 'geonaute',
        62 : 'id_bike',
        63 : 'specialized',
        64 : 'wtek',
        65 : 'physical_enterprises',
        66 : 'north_pole_engineering',
        67 : 'bkool',
        68 : 'cateye',
        69 : 'stages_cycling',
        70 : 'sigmasport',
        71 : 'tomtom',
        72 : 'peripedal',
        73 : 'wattbike',
        76 : 'moxy',
        77 : 'ciclosport',
        78 : 'powerbahn',
        79 : 'acorn_projects_aps',
        80 : 'lifebeam',
        81 : 'bontrager',
        82 : 'wellgo',
        83 : 'scosche',
        84 : 'magura',
        85 : 'woodway',
        86 : 'elite',
        87 : 'nielsen_kellerman',
        88 : 'dk_city',
        89 : 'tacx',
        90 : 'direction_technology',
        91 : 'magtonic',
        92 : '1partcarbon',
        93 : 'inside_ride_technologies',
        94 : 'sound_of_motion',
        95 : 'stryd',
        96 : 'icg',
        97 : 'MiPulse',
        98 : 'bsx_athletics',
        99 : 'look',
        100 : 'campagnolo_srl',
        101 : 'body_bike_smart',
        102 : 'praxisworks',
        103 : 'limits_technology',
        104 : 'topaction_technology',
        105 : 'cosinuss',
        106 : 'fitcare',
        107 : 'magene',
        108 : 'giant_manufacturing_co',
        109 : 'tigrasport',
        110 : 'salutron',
        255 : 'development',
        257 : 'healthandlife',
        258 : 'lezyne',
        259 : 'scribe_labs',
        260 : 'zwift',
        261 : 'watteam',
        262 : 'recon',
        263 : 'favero_electronics',
        264 : 'dynovelo',
        265 : 'strava',
        266 : 'precor',
        267 : 'bryton',
        268 : 'sram',
        269 : 'navman',
        270 : 'cobi',
        271 : 'spivi',
        272 : 'mio_magellan',
        273 : 'evesports',
        274 : 'sensitivus_gauge',
        275 : 'podoon',
        276 : 'life_time_fitness',
        277 : 'falco_e_motors',
        5759 : 'actigraphcorp'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='manufacturer', *args, **kwargs)


class GarminProductField(EnumField):
    enum = {
        1 : 'hrm1',
        2 : 'axh01',
        3 : 'axb01',
        4 : 'axb02',
        5 : 'hrm2ss',
        6 : 'dsi_alf02',
        7 : 'hrm3ss',
        8 : 'hrm_run_single_byte_product_id',
        9 : 'Bike Speed Sensor',
        10 : 'Bike Cadence Sensor',
        11 : 'axs01',
        12 : 'hrm_tri_single_byte_product_id',
        14 : 'fr225_single_byte_product_id',
        473 : 'fr301_china',
        474 : 'fr301_japan',
        475 : 'fr301_korea',
        494 : 'fr301_taiwan',
        717 : 'fr405',
        782 : 'fr50',
        987 : 'fr405_japan',
        988 : 'fr60',
        1011 : 'dsi_alf01',
        1018 : 'fr310xt',
        1036 : 'edge500',
        1124 : 'fr110',
        1169 : 'edge800',
        1199 : 'edge500_taiwan',
        1213 : 'edge500_japan',
        1253 : 'chirp',
        1274 : 'fr110_japan',
        1325 : 'edge200',
        1328 : 'fr910xt',
        1333 : 'edge800_taiwan',
        1334 : 'edge800_japan',
        1341 : 'alf04',
        1345 : 'fr610',
        1360 : 'fr210_japan',
        1380 : 'vector_ss',
        1381 : 'vector_cp',
        1386 : 'edge800_china',
        1387 : 'edge500_china',
        1410 : 'fr610_japan',
        1422 : 'edge500_korea',
        1436 : 'fr70',
        1446 : 'fr310xt_4t',
        1461 : 'amx',
        1482 : 'fr10',
        1497 : 'edge800_korea',
        1499 : 'swim',
        1537 : 'fr910xt_china',
        1551 : 'fenix',
        1555 : 'edge200_taiwan',
        1561 : 'edge510',
        1567 : 'edge810',
        1570 : 'tempe',
        1600 : 'fr910xt_japan',
        1623 : 'fr620',
        1632 : 'fr220',
        1664 : 'fr910xt_korea',
        1688 : 'fr10_japan',
        1721 : 'edge810_japan',
        1735 : 'virb_elite',
        1736 : 'edge_touring',
        1742 : 'edge510_japan',
        1743 : 'HRM-Tri',
        1752 : 'hrm_run',
        1765 : 'fr920xt',
        1821 : 'edge510_asia',
        1822 : 'edge810_china',
        1823 : 'edge810_taiwan',
        1836 : 'edge1000',
        1837 : 'vivo_fit',
        1853 : 'virb_remote',
        1885 : 'vivo_ki',
        1903 : 'fr15',
        1907 : 'vivo_active',
        1918 : 'edge510_korea',
        1928 : 'fr620_japan',
        1929 : 'fr620_china',
        1930 : 'fr220_japan',
        1931 : 'fr220_china',
        1936 : 'approach_s6',
        1956 : 'vivo_smart',
        1967 : 'fenix2',
        1988 : 'epix',
        2050 : 'fenix3',
        2052 : 'edge1000_taiwan',
        2053 : 'edge1000_japan',
        2061 : 'fr15_japan',
        2067 : 'edge520',
        2070 : 'edge1000_china',
        2072 : 'fr620_russia',
        2073 : 'fr220_russia',
        2079 : 'vector_s',
        2100 : 'edge1000_korea',
        2130 : 'fr920xt_taiwan',
        2131 : 'fr920xt_china',
        2132 : 'fr920xt_japan',
        2134 : 'virbx',
        2135 : 'vivo_smart_apac',
        2140 : 'etrex_touch',
        2147 : 'edge25',
        2148 : 'fr25',
        2150 : 'vivo_fit2',
        2153 : 'fr225',
        2156 : 'fr630',
        2157 : 'fr230',
        2160 : 'vivo_active_apac',
        2161 : 'vector_2',
        2162 : 'vector_2s',
        2172 : 'virbxe',
        2173 : 'fr620_taiwan',
        2174 : 'fr220_taiwan',
        2175 : 'truswing',
        2188 : 'fenix3_china',
        2189 : 'fenix3_twn',
        2192 : 'varia_headlight',
        2193 : 'varia_taillight_old',
        2204 : 'edge_explore_1000',
        2219 : 'fr225_asia',
        2225 : 'varia_radar_taillight',
        2226 : 'varia_radar_display',
        2238 : 'edge20',
        2262 : 'd2_bravo',
        2266 : 'approach_s20',
        2276 : 'varia_remote',
        2327 : 'hrm4_run',
        2337 : 'VivoActive HR',
        2347 : 'vivo_smart_gps_hr',
        2348 : 'vivo_smart_hr',
        2368 : 'vivo_move',
        2398 : 'varia_vision',
        2406 : 'vivo_fit3',
        2413 : 'fenix3_hr',
        2429 : 'index_smart_scale',
        2431 : 'fr235',
        2432 : 'Fenix 3 Chronos',
        2441 : 'oregon7xx',
        2444 : 'rino7xx',
        2496 : 'nautix',
        2530 : 'edge_820',
        2531 : 'edge_explore_820',
        2544 : 'Fenix 5s',
        2593 : 'Running Dynamics Pod',
        2604 : 'Fenix 5X',
        2606 : 'VivoFit Jr',
        2691 : 'FR935',
        2697 : 'Fenix 5 Sapphire',
        2700 : 'VivoActive 3',
        10007 : 'Foot Pod (sdm4)',
        10014 : 'edge_remote',
        20119 : 'training_center',
        65531 : 'connectiq_simulator',
        65532 : 'android_antplus_plugin',
        65534 : 'connect'
    }

class WahooFitnessProductField(EnumField):
    enum = {
        6 : 'RPM Sensor',
    }

class ProductField(EnumField):
    dependant_field_control_fields = ['manufacturer']

    _manufacturer_to_product_fields = {
        'Garmin'        : GarminProductField,
        'Wahoo Fitness' : WahooFitnessProductField,
    }

    def dependant_field(self, control_value_list):
        manufacturer = control_value_list[0]
        try:
            dependant_field_name = self._manufacturer_to_product_fields[manufacturer]
        except:
            dependant_field_name = Field
        return dependant_field_name(name='product')


class DisplayOrientationField(EnumField):
    enum = {
        0 : 'auto',
        1 : 'portrait',
        2 : 'landscape',
        3 : 'portrait_flipped',
        4 : 'landscape_flipped',
        255 : 'invalid'
    }


class SideField(EnumField):
    enum = {
        0 : 'right',
        1 : 'left',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='side', *args, **kwargs)


class BacklightModeField(EnumField):
    enum = {
        0 : 'off',
        1 : 'manual',
        2 : 'key_and_messages',
        3 : 'auto_brightness',
        4 : 'smart_notifications',
        5 : 'key_and_messages_night',
        6 : 'key_and_messages_and_smart_notifications',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='backlight_mode', *args, **kwargs)


class AntNetworkField(EnumField):
    enum = {
        0 : 'public',
        1 : 'ant+',
        2 : 'antfs',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='ant_network', *args, **kwargs)


class SourceTypeField(EnumField):
    enum = {
        0 : 'ant',
        1 : 'ant+',
        2 : 'bluetooth',
        3 : 'bluetooth_low_energy',
        4 : 'wifi',
        5 : 'local',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='source_type', *args, **kwargs)


class BatteryVoltageField(Field):
    _units = [ 'v', 'v' ]
    _conversion_factor = [ 256.0, 256.0 ]


class BatteryStatusField(EnumField):
    enum = {
        1 : 'new',
        2 : 'good',
        3 : 'ok',
        4 : 'low',
        5 : 'critical',
        6 : 'charging',
        7 : 'unknown',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='battery_status', *args, **kwargs)


class AutoSyncFrequencyField(EnumField):
    enum = {
        0 : 'never',
        1 : 'occasionally',
        2 : 'frequent',
        3 : 'once_a_day',
        4 : 'remote',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='auto_sync_frequency', *args, **kwargs)


class BodyLocationField(EnumField):
    enum = {
        0 : 'left_leg',
        1 : 'left_calf',
        2 : 'left_shin',
        3 : 'left_hamstring',
        4 : 'left_quad',
        5 : 'left_glute',
        6 : 'right_leg',
        7 : 'right_calf',
        8 : 'right_shin',
        9 : 'right_hamstring',
        10 : 'right_quad',
        11 : 'right_glut',
        12 : 'torso_back',
        13 : 'left_lower_back',
        14 : 'left_upper_back',
        15 : 'right_lower_back',
        16 : 'right_upper_back',
        17 : 'torso_front',
        18 : 'left_abdomen',
        19 : 'left_chest',
        20 : 'right_abdomen',
        21 : 'right_chest',
        22 : 'left_arm',
        23 : 'left_shoulder',
        24 : 'left_bicep',
        25 : 'left_tricep',
        26 : 'left_brachioradialis',
        27 : 'left_forearm_extensors',
        28 : 'right_arm',
        29 : 'right_shoulder',
        30 : 'right_bicep',
        31 : 'right_tricep',
        32 : 'right_brachioradialis',
        33 : 'right_forearm_extensors',
        34 : 'neck',
        35 : 'throat',
        36 : 'waist_mid_back',
        37 : 'waist_front',
        38 : 'waist_left',
        39 : 'waist_right',
        255 : 'invalid'
    }


class AutoActivityDetectField(BitField):
    bits = {
        0x00000000 : 'none',
        0x00000001 : 'running',
        0x00000002 : 'cycling',
        0x00000004 : 'swimming',
        0x00000008 : 'walking',
        0x00000020 : 'elliptical',
        0x00000400 : 'sedentary',
        0xffffffff : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        BitField.__init__(self, name='auto_activity_detect', *args, **kwargs)


class MessageIndexField(Field):
    def convert_single(self, value, invalid):
        converted_value = {}
        converted_value['selected'] = ((value & 0x8000) == 0x8000)
        converted_value['value'] = (value & 0x0FFF)
        return converted_value

#
# User related fields
#
class GenderField(EnumField):
    enum = {0 : 'female', 1 : 'male' }


class HeightField(DistanceMetersField):
    #_conversion_factor = [ 100.0, 30.48 ]
    def __init__(self, *args, **kwargs):
        DistanceMetersField.__init__(self, name='height', scale=100.0, *args, **kwargs)


class WeightField(Field):
    _units = [ 'kg', 'lbs' ]
    _conversion_factor = [ 10.0, 4.545 ]


class CaloriesField(Field):
    _units = [ 'kcal', 'kcal' ]


class ActiveCaloriesField(CaloriesField):
    def __init__(self, *args, **kwargs):
        CaloriesField.__init__(self, name='active_calories', *args, **kwargs)


class CaloriesDayField(Field):
    _units = [ 'kcal/day', 'kcal/day' ]
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)


class CyclesCaloriesField(Field):
    _units = [ 'kcal/cycle', 'kcal/cycle' ]
    _conversion_factor = [ 5019.6, 5019.6 ]
    def __init__(self):
        Field.__init__(self, 'cycles_to_calories')


class CyclesDistanceField(Field):
    _units = [ 'm/cycle', 'm/cycle' ]
    _conversion_factor = [ 5000.0, 5000.0 ]
    def __init__(self):
        Field.__init__(self, 'cycles_to_distance')


class HeartRateField(Field):
    _units = [ 'bpm', 'bpm' ]
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)

class HeartRateZoneCalcField(EnumField):
    enum = {
        0 : 'custom',
        1 : 'percent_max_hr',
        2 : 'percent_hrr',
        255 : 'invalid'
    }
    def __init__(self):
        EnumField.__init__(self, 'hr_calc_type')


class PowerCalcField(EnumField):
    enum = {
        0 : 'custom',
        1 : 'percent_ftp',
        255 : 'invalid'
    }
    def __init__(self):
        EnumField.__init__(self, 'pwr_calc_type')


class LanguageField(EnumField):
    enum = {
        0 :'English',
        1 : 'French',
        2 : 'Italian',
        3 : 'German',
        4 : 'Spanish',
        5 : 'Croation',
        6 : 'Czech',
        7 : 'Danish',
        8 : 'Dutch',
        9 : 'Finnish',
        10 : 'Greek',
        11 : 'Hungarian',
        12 : 'Norwegian',
        13 : 'Polish',
        14 : 'Portuguese',
        15 : 'Slovakian',
        16 : 'Slovenian',
        17 : 'Swedish',
        18 : 'Russian',
        19 : 'Turkish',
        20 : 'Latvian',
        21 : 'Ukranian',
        22 : 'Arabic',
        23 : 'Farsi',
        24 : 'Bulgarian',
        25 : 'Romanian',
        26 : 'Chinese',
        27 : 'Japanese',
        28 : 'Korean',
        29 : 'Taiwanese',
        30 : 'Thai',
        31 : 'Hebrew',
        32 : 'Brazialn_Portuguese',
        33 : 'Indonesian',
        34 : 'Maylasian',
        35 : 'Vietnamese',
        36 : 'Burmese',
        37 : 'Mongolian',
        254 : 'Custom',
        255 : 'Invalid'
    }


#
# Time related fields
#
class DateModeField(EnumField):
    enum = {
        0 : 'day_month',
        1 : 'month_day',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='date_mode', *args, **kwargs)


class TimeModeField(EnumField):
    enum = {
        0 : '12_hour',
        1 : '24_hour',
        2 : 'military',
        3 : '12_hour_secs',
        4 : '24_hour_secs',
        5 : 'utc',
        255 : 'invalid'
    }
    def __init__(self, *args, **kwargs):
        EnumField.__init__(self, name='time_mode', *args, **kwargs)


class TimestampField(Field):
    def __init__(self, name='timestamp', utc=True):
        self.utc = utc
        Field.__init__(self, name)

    def convert_single(self, value, invalid):
        if self.utc:
            timestamp = time.time()
            time_now = datetime.datetime.fromtimestamp(timestamp)
            time_utc = datetime.datetime.utcfromtimestamp(timestamp)
            utc_offset_secs = (time_now - time_utc).total_seconds()
            # hack - summary of the day messages appear at midnight and we want them to appear in the current day,
            # reimplement properly
            value += (utc_offset_secs - 1)
        return datetime.datetime(1989, 12, 31, 0, 0, 0) +  datetime.timedelta(0, value)


class TimeMsField(Field):
    def __init__(self, name='time_ms', scale=1.0, utc=True):
        self._conversion_factor = scale
        Field.__init__(self, name)

    def convert_single(self, value, invalid):
        if value == invalid:
            return None
        return Conversions.ms_to_dt_time(value / self._conversion_factor)


class CumActiveTimeField(TimeMsField):
    def __init__(self, *args, **kwargs):
        TimeMsField.__init__(self, name='cum_active_time', *args, **kwargs)


class TimeSField(Field):
    _units = [ 's', 's' ]


class TimeMinField(Field):
    def convert_single(self, value, invalid):
        if value == invalid:
            return None
        return Conversions.min_to_dt_time(value)


class TimeOfDayField(Field):
    def convert_single(self, value, invalid):
        if value == invalid:
            return None
        return Conversions.secs_to_dt_time(value)


class DurationField(TimeMinField):
    def __init__(self, *args, **kwargs):
        TimeMinField.__init__(self, name='duration', *args, **kwargs)


class MonitoringDistanceField(DistanceMetersField):
    def __init__(self, *args, **kwargs):
        DistanceMetersField.__init__(self, name='distance', *args, **kwargs)


class SpeedKphField(Field):
    _units = [ 'km/h', 'm/h' ]
    _conversion_factor = [ 277.8, 172.6 ]


class SpeedMpsField(Field):
    _units = [ 'kmph', 'mph' ]
    _conversion_factor = [ 277.77, 447.04 ]


class CyclesField(Field):
    _units = ['cycles', 'cycles' ]
    def __init__(self, name, scale=2.0, *args, **kwargs):
        self. _conversion_factor = [ scale, scale ]
        Field.__init__(self, name)


class FractionalCyclesField(Field):
    _units = ['cycles', 'cycles' ]
    _conversion_factor = [ 128.0, 128.0 ]


class StepsField(Field):
    _units = ['steps', 'steps' ]
    def __init__(self, name, scale=1.0, *args, **kwargs):
        self. _conversion_factor = [ scale, scale ]
        Field.__init__(self, name)


class StrokesField(Field):
    _units = ['strokes', 'strokes' ]
    def __init__(self, name, scale=2.0, *args, **kwargs):
        self. _conversion_factor = [ scale, scale ]
        Field.__init__(self, name)


def cycles_units_to_field(name):
    field_mapping = {
        'cycles' : CyclesField,
        'steps' : StepsField,
        'strokes' : StrokesField,
    }
    try:
        return field_mapping[name]
    except:
        return CyclesField


def cycles_activity_to_units(activity):
    _units = {
        'generic' : 'cycles',
        # steps activities
        'walking' : 'steps',
        'running' : 'steps',
        'hiking' : 'steps',
        'elliptical' : 'steps',
        # strokes activities
        'cycling' : 'strokes',
        'swimming' : 'strokes',
        'rowing' : 'strokes',
        'paddling' : 'strokes',
        'stand_up_paddleboarding' : 'strokes',
        'kayaking' : 'strokes',
    }
    try:
        return _units[activity]
    except:
        return _units['generic']


class ActivityBasedCyclesField(Field):
    _units = ['cycles', 'cycles' ]
    _conversion_factor = [ 2.0, 2.0 ]
    dependant_field_control_fields = ['activity_type']

    def __init__(self, *args, **kwargs):
        Field.__init__(self, name='cycles', *args, **kwargs)

    def dependant_field(self, control_value_list):
        activity_type = control_value_list[0]
        dependant_field_name_base = cycles_activity_to_units(activity_type)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return cycles_units_to_field(dependant_field_name_base)(name=dependant_field_name)


class ActivityField(Field):
    _type = { 0 : 'manual', 1 : 'auto_multi_sport' }

    def convert_single(self, value, invalid):
        try:
            return ActivityField._type[value]
        except:
            return value


class ActivityTypeField(Field):
    _type = {
        0 : 'generic',
        1 : 'running',
        2 : 'cycling',
        3 : 'transition',
        4 : 'fitness_equipment',
        5 : 'swimming',
        6 : 'walking',
        7 : 'sedentary',
        8 : 'stop_disable',
        9 : 'unknown',
        245 : 'all'
    }
    def __init__(self):
        Field.__init__(self, 'activity_type')

    def convert_single(self, value, invalid):
        return ActivityTypeField._type[value]

    def convert_single_units(self, value, invalid):
        return cycles_activity_to_units(ActivityTypeField._type[value])


class ActivityClassField(Field):
    def convert_single(self, value, invalid):
        if value & 0x80:
            activity_class = "athlete "
        else:
            activity_class = ""
        activity_class += str(value & 0x7f)
        return activity_class


class IntensityField(Field):
    _max_intensity = 8
    def __init__(self, *args, **kwargs):
        Field.__init__(self, "intensity", *args, **kwargs)


class ActivityTypeIntensityField(Field):
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)
        self._subfield['activity_type'] = ActivityTypeField()
        self._subfield['intensity'] = IntensityField()

    def convert(self, value, invalid, english_units=False):
        activity_type = value & 0x1f
        intensity = value >> 5
        return FieldValue(self, ['activity_type', 'intensity'],
                          invalid=invalid, value=self.convert_many(value, invalid), orig=value,
                          activity_type=self._subfield['activity_type'].convert(activity_type, 0xff, english_units),
                          intensity=self._subfield['intensity'].convert(intensity, 0xff, english_units))


class FileField(EnumField):
    enum = {
        0 : 'unknown0',
        1 : 'device',
        2 : 'settings',
        3 : 'sport_settings',
        4 : 'activity',
        5 : 'workout',
        6 : 'course',
        7 : 'schedules',
        9 : 'weight',
        10 : 'totals',
        11 : 'goals',
        14 : 'blood_pressure',
        15 : 'monitoring_a',
        20 : 'activity_summary',
        28 : 'monitoring_daily',
        32 : 'monitoring_b',
        34 : 'segment',
        35 : 'segment_list',
        40 : 'exd_configuration',
        44 : 'unknown44',
        64 : 'unknown64',
        255 : 'invalid'
    }


class VersionField(Field):
    _conversion_factor = [ 100.0, 100.0 ]
    def __init__(self, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)


class EventField(EnumField):
    enum = {
        0 : 'timer',
        3 : 'workout',
        4 : 'workout_step',
        5 : 'power_down',
        6 : 'power_up',
        7 : 'off_course',
        8 : 'session',
        9 : 'lap',
        10 : 'course_point',
        11 : 'battery',
        12 : 'virtual_partner_pace',
        13 : 'hr_high_alert',
        14 : 'hr_low_alert',
        15 : 'speed_high_alert',
        16 : 'speed_low_alert',
        17 : 'cad_high_alert',
        18 : 'cad_low_alert',
        19 : 'power_high_alert',
        20 : 'power_low_alert',
        21 : 'recovery_hr',
        22 : 'battery_low',
        23 : 'time_duration_alert',
        24 : 'distance_duration_alert',
        25 : 'calorie_duration_alert',
        26 : 'activity',
        27 : 'fitness_equipment',
        28 : 'length',
        32 : 'user_marker',
        33 : 'sport_point',
        36 : 'calibration',
        41 : 'unknown',
        42 : 'front_gear_change',
        43 : 'rear_gear_change',
        44 : 'rider_position_change',
        45 : 'elev_high_alert',
        46 : 'elev_low_alert',
        47 : 'comm_timeout'
    }


class EventTypeField(EnumField):
    enum = {
        0 : 'start',
        1 : 'stop',
        2 : 'consecutive_depreciated',
        3 : 'marker',
        4 : 'stop_all',
        5 : 'begin_depreciated',
        6 : 'end_depreciated',
        7 : 'end_all_depreciated',
        8 : 'stop_disable',
        9 : 'stop_disable_all'
    }

class EventDataField(Field):
    _dependant_field = {
        'timer' : Field('timer_trigger'),
        245 : CyclesField
    }
    dependant_field_control_fields = ['event']

    def __init__(self, *args, **kwargs):
        Field.__init__(self, name='event_data', *args, **kwargs)

    def dependant_field(self, control_value_list):
        event = control_value_list[0]
        return EventDataField._dependant_field[event]


class LapTriggerField(EnumField):
    enum = { 0 : 'manual', 1 : 'time', 2 : 'distance', 3 : 'position_start', 4 : 'position_lap',
              5 : 'position_waypoint', 6 : 'position_marked', 7 : 'session_end', 8 : 'fitness_equipment' }


class SessionTriggerField(EnumField):
    enum = { 0 : 'activity_end', 1 : 'manual', 2 : 'auto_multi_sport', 3 : 'fitness_equipment' }



class SportBasedCyclesField(Field):
    _units = ['cycles', 'cycles' ]
    _conversion_factor = [ 1.0, 1.0 ]
    dependant_field_control_fields = ['sport', 'sub_sport']
    _scale = {
        'cycles'    : 1.0,
        'steps'     : 0.5,
        'strokes'   : 1.0
    }
    def dependant_field(self, control_value_list):
        sport = control_value_list[0]
        dependant_field_name_base = cycles_activity_to_units(sport)
        if dependant_field_name_base == 'cycles':
            sub_sport = control_value_list[1]
            dependant_field_name_base = cycles_activity_to_units(sub_sport)
        dependant_field_name = self.name.replace('cycles', dependant_field_name_base)
        return cycles_units_to_field(dependant_field_name_base)(dependant_field_name, self._scale[dependant_field_name_base])


class SportField(EnumField):
    enum = {
        0 : 'generic',
        1 : 'running',
        2 : 'cycling',
        3 : 'transition',
        4 : 'fitness_equipment',
        5 : 'swimming',
        6 : 'basketball',
        7 : 'soccer',
        8 : 'tennis',
        9 : 'american_football',
        10 : 'training',
        11 : 'walking',
        12 : 'cross_country_skiing',
        13 : 'alpine_skiing',
        14 : 'snowboarding',
        15 : 'rowing',
        16 : 'mountaineering',
        17 : 'hiking',
        18 : 'multisport',
        19 : 'paddling',
        20 : 'flying',
        21 : 'e_biking',
        22 : 'motorcycling',
        23 : 'boating',
        24 : 'driving',
        25 : 'golf',
        26 : 'hang_gliding',
        27 : 'horseback_riding',
        28 : 'hunting',
        29 : 'fishing',
        30 : 'inline_skating',
        31 : 'rock_climbing',
        32 : 'sailing',
        33 : 'ice_skating',
        34 : 'sky_diving',
        35 : 'snowshoeing',
        36 : 'snowmobiling',
        37 : 'stand_up_paddleboarding',
        38 : 'surfing',
        39 : 'wakeboarding',
        40 : 'water_skiing',
        41 : 'kayaking',
        42 : 'rafting',
        43 : 'windsurfing',
        44 : 'kitesurfing',
        45 : 'tactical',
        46 : 'jumpmaster',
        47 : 'boxing',
        48 : 'floor_climbing'
    }
    _units = {
        0 : 'cycles',
        1 : 'steps',
        2 : 'strokes',
        5 : 'strokes',
        11 : 'steps',
        15 : 'strokes',
        17 : 'steps',
        19 : 'strokes',
        37 : 'strokes',
    }
    def __init__(self, *args, **kwargs):
        Field.__init__(self, name='sport', *args, **kwargs)

    @classmethod
    def get_units(cls, sport_index):
        try:
            return cls._units[sport_index]
        except:
            return cls._units[0]


class SubSportField(EnumField):
    enum = {
        0 : 'generic',
        1 : 'treadmill',
        2 : 'street',
        3 : 'trail',
        4 : 'track',
        5 : 'spin',
        6 : 'indoor_cycling',
        7 : 'road',
        8 : 'mountain',
        9 : 'downhill',
        10 : 'recumbent',
        11 : 'cyclocross',
        12 : 'hand_cycling',
        13 : 'track_cycling',
        14 : 'indoor_rowing',
        15 : 'elliptical',
        16 : 'stair_climbing',
        17 : 'lap_swimming',
        18 : 'open_water',
        19 : 'flexibility_training',
        20 : 'strength_training',
        21 : 'warm_up',
        22 : 'match',
        23 : 'exercise',
        24 : 'challenge',
        25 : 'indoor_skiing',
        26 : 'cardio_training',
        27 : 'indoor_walking',
        28 : 'e_bike_fitness',
        29 : 'bmx',
        30 : 'casual_walking',
        31 : 'speed_walking',
        32 : 'bike_to_run_transition',
        33 : 'run_to_bike_transition',
        34 : 'swim_to_bike_transition',
        35 : 'atv',
        36 : 'motocross',
        37 : 'backcountry',
        38 : 'resort',
        39 : 'rc_drone',
        40 : 'wingsuit',
        41 : 'whitewater',
        42 : 'skate_skiing',
        43 : 'yoga',
        44 : 'pilates',
        45 : 'indoor_running',
        46 : 'gravel_cycling',
        47 : 'e_bike_mountain',
        48 : 'commuting',
        49 : 'mixed_surface',
        50 : 'navigate',
        51 : 'track_me',
        52 : 'map',
        254 : 'all'
    }
    def __init__(self, *args, **kwargs):
        Field.__init__(self, name='sub_sport', *args, **kwargs)


class PosField(Field):
    _units = [ 'degrees', 'degrees' ]
    _conversion_factor = [ 11930326.891, 11930326.891 ]


class CadenceField(Field):
    _units = [ 'rpm', 'rpm' ]


class FractionalCadenceField(Field):
    _units = [ 'rpm', 'rpm' ]
    _conversion_factor = [ 128.0, 128.0 ]


class PowerField(Field):
    _units = [ 'watts', 'watts' ]


class WorkField(Field):
    _units = [ 'J', 'J' ]


class AltitudeField(Field):
    _units = [ 'm', 'ft' ]
    _conversion_factor = [ 13.986, 4.262 ]


class EnhancedAltitudeField(Field):
    _units = [ 'm', 'ft' ]
    _conversion_factor = [ 6993, 2131 ]


class ClimbField(Field):
    _units = [ 'm', 'ft' ]
    _conversion_factor = [ 1000.0, 304.79 ]


class ClimbMetersField(DistanceMetersField):
    _units = [ 'm', 'ft' ]


class TemperatureField(Field):
    _units = [ 'C', 'F' ]
    _conversion_factor = [ 1, 0.55555555556 ]
    _conversion_constant = [ 0, 32 ]


class TrainingeffectField(Field):
    _conversion_factor = [ 10.0, 10.0 ]
