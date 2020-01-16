"""Enums that represent FIT file message product field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from Fit.field_enums import FuzzyFieldEnum, UnknownEnumValue
from Fit.manufacturer import Manufacturer


class GarminProduct(FuzzyFieldEnum):
    """Garmin product codes used in FIT files."""

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
    GPS_1619                        = 1619
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
    Forerunner_630                  = 2156
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
    Fenix_5S                        = 2544
    D2_Bravo_Titanium               = 2547
    Varia_UT800                     = 2567
    Running_Dynamics_Pod            = 2593
    Fenix5X                         = 2604
    VivoFit_Jr                      = 2606
    VivoSport                       = 2623
    Forerunner935                   = 2691
    Fenix_5_Sapphire                = 2697
    VivoActive_3                    = 2700
    Edge_1030                       = 2713
    VivoMove_HR                     = 2772
    Approach_z80                    = 2806
    VivoSmart3_Apac                 = 2831
    VivoSport_Apac                  = 2832
    Descent                         = 2859
    Forerunner_645                  = 2886
    Forerunner_645m                 = 2888
    Fenix_5S_Plus                   = 2900
    Edge_130                        = 2909
    Vivosmart_4                     = 2927
    GPS_2957                        = 2957
    Approach_x10                    = 2962
    VivoActive_3m_w                 = 2988
    Edge_Explore                    = 3011
    GPSMap66                        = 3028
    Approach_S10                    = 3049
    VivoActive_3M_l                 = 3066
    Approach_G80                    = 3085
    GPS_3107                        = 3107
    Fenix_5_Plus                    = 3110
    Fenix_5x_Plus                   = 3111
    Edge_520_Plus                   = 3112
    Instinct                        = 3126
    Fenix_6S_Pro                    = 3288
    Fenix_6                         = 3289
    sesnor_hub_3294                 = 3294
    HRM_Dual                        = 3299
    Approach_S40                    = 3314
    FootPod_SDM4                    = 10007
    edge_remote                     = 10014
    Training_Center                 = 20119
    Connectiq_Simulator             = 65531
    Android_Antplus_plugin          = 65532
    connect                         = 65534
    invalid                         = 65535


class GarminLocalProduct(FuzzyFieldEnum):
    """Garmin product codes used in FIT files for sub-devices."""

    Bluetooth_Low_Energy_Chipset    = 0
    Accelerometer_12                = 12
    Accelerometer_16                = 16
    Accelerometer_18                = 18
    GPS_1619                        = 1619
    GPS_1620                        = 1620
    GPS_1621                        = 1621
    GPS_2957                        = 2957
    Accelerometer_8194              = 8194
    Accelerometer_8195              = 8195
    Accelerometer_12529             = 12529
    Accelerometer_12533             = 12533
    Accelerometer_16150             = 16150
    Accelerometer_16155             = 16155
    Accelerometer_16310             = 16310
    Accelerometer_16423             = 16423
    Accelerometer_16427             = 16427
    Accelerometer_16354             = 16354
    Accelerometer_17350             = 17530
    Accelerometer_21909             = 21909
    BTLE_Chipset                    = 24832


class WahooFitnessProduct(FuzzyFieldEnum):
    """Wahoo Fitness product codes used in FIT files."""

    RPM_Sensor                      = 6


class ScoscheProduct(FuzzyFieldEnum):
    """Scosche product codes used in FIT files."""

    Rhythm_Plus_Armband_HRM         = 2


class UnknownProduct(UnknownEnumValue):
    """Unknown product codes used in FIT files."""

    def __init__(self, index):
        UnknownEnumValue.__init__(self, 'UnknownProduct', index)


def product_enum(manufacturer, product_str):
    """Return a product enum given the manufacturer enum and a product string."""
    _manufacturer_to_product_enum = {
        Manufacturer.Garmin                 : GarminProduct,
        Manufacturer.Garmin_local           : GarminLocalProduct,
        Manufacturer.Dynastream             : GarminProduct,
        Manufacturer.Dynastream_OEM         : GarminProduct,
        Manufacturer.Scosche                : ScoscheProduct,
        Manufacturer.Wahoo_Fitness          : WahooFitnessProduct,
        Manufacturer.invalid                : GarminProduct,
    }
    return _manufacturer_to_product_enum[manufacturer].from_string(product_str)
