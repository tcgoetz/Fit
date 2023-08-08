"""Enums that represent FIT file message product field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from .field_enums import FuzzyFieldEnum, UnknownEnumValue
from .manufacturer import Manufacturer


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
    hrm4_run_single_byte_product_id = 13
    fr225_single_byte_product_id    = 14
    Bike_Speed_Sensor_Gen3_sb       = 15
    Bike_Cadence_Sensor_Gen3_sb     = 16
    Bike_Cadence_Sensor_V2          = 20
    Optical_Heart_Rate_Sensor       = 255
    ForeRunner_301_China            = 473
    ForeRunner_301_Japan            = 474
    ForeRunner_301_Korea            = 475
    ForeRunner_301_Taiwan           = 494
    ForeRunner_405                  = 717
    ForeRunner_50                   = 782
    ForeRunner_405_Japan            = 987
    ForeRunner_60                   = 988
    dsi_alf01                       = 1011
    ForeRunner_310xt                = 1018
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
    ForeRunner_610                  = 1345
    ForeRunner_210_Japan            = 1360
    vector_ss                       = 1380
    vector_cp                       = 1381
    edge800_china                   = 1386
    edge500_china                   = 1387
    Approach_G10                    = 1405
    fr610_japan                     = 1410
    edge500_korea                   = 1422
    fr70                            = 1436
    fr310xt_4t                      = 1446
    amx                             = 1461
    ForeRunner_10                   = 1482
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
    fr735xt                         = 2158
    vivo_active_apac                = 2160
    vector_2                        = 2161
    vector_2s                       = 2162
    virbxe                          = 2172
    fr620_taiwan                    = 2173
    fr220_taiwan                    = 2174
    truswing                        = 2175
    d2airvenu                       = 2187
    Fenix3_china                    = 2188
    Fenix3_twn                      = 2189
    varia_headlight                 = 2192
    varia_taillight_old             = 2193
    edge_explore_1000               = 2204
    fr225_asia                      = 2219
    varia_radar_taillight           = 2225
    varia_radar_display             = 2226
    edge20                          = 2238
    Edge_520_Asia                   = 2260
    Edge_520_Japan                  = 2261
    D2_Bravo                        = 2262
    approach_s20                    = 2266
    VivoSmart_2                     = 2271
    Edge_1000_Thai                  = 2274
    varia_remote                    = 2276
    Edge_25_Asia                    = 2288
    Edge_25_Japan                   = 2289
    Edge_20_Asia                    = 2290
    Approach_X40                    = 2292
    Fenix_3_Japan                   = 2293
    VivoSmart_emea                  = 2294
    ForeRunner_630_Asia             = 2310
    ForRunner_630_Japan             = 2311
    ForeRunner_230_Japan            = 2313
    HRM4_Run                        = 2327
    Epix_Japan                      = 2332
    VivoActive_HR                   = 2337
    VivoSmart_GPS_HR                = 2347
    VivoSmart_HR                    = 2348
    VivoSmart_HR_Asia               = 2361
    VivoSmart_GPS_HR_Asia           = 2362
    Varia_Taillight                 = 2379
    VivoMove                        = 2368
    ForeRunner_235_Asia             = 2396
    ForeRunner_235_Japan            = 2397
    varia_vision                    = 2398
    VivoFit3                        = 2406
    Fenix_3_Korea                   = 2407
    Fenix_3_Sea                     = 2408
    Virb_Ultra_30                   = 2417
    Fenix3_HR                       = 2413
    Index_Smart_Scale               = 2429
    fr235                           = 2431
    Fenix3_Chronos                  = 2432
    Oregon7xx                       = 2441
    Rino_7xx                        = 2444
    Fenix_3_HR_China                = 2473
    Fenix_3_HR_Taiwan               = 2474
    Fenix_3_HR_Japan                = 2475
    Fenix_3_HR_Sea                  = 2476
    Fenix_3_HR_Korea                = 2477
    nautix                          = 2496
    VivoActive_HR_APAC              = 2497
    Forerunner35                    = 2503
    Oregon_7xx_ww                   = 2512
    Edge_820                        = 2530
    Edge_Explore_820                = 2531
    ForeRunner_735xt_APAC           = 2533
    ForeRunner_735xt_Japan          = 2534
    Fenix_5S                        = 2544
    D2_Bravo_Titanium               = 2547
    Epix_Korea                      = 2457
    Varia_UT800                     = 2567
    Running_Dynamics_Pod            = 2593
    Edge_820_China                  = 2599
    Edge_820_Japan                  = 2600
    Fenix5X                         = 2604
    VivoFit_Jr                      = 2606
    VivoSmart_3                     = 2622
    VivoSport                       = 2623
    Edge_820_Taiwan                 = 2628
    Edge_820_Korea                  = 2629
    Edge_820_Sea                    = 2630
    ForeRunner_35_Hebrew            = 2650
    Approach_S60                    = 2656
    ForeRunner_35_apac              = 2667
    ForeRunner_35_Japan             = 2668
    Fenix_3_Chronos_Asia            = 2675
    Virb_360                        = 2687
    Forerunner935                   = 2691
    Fenix_5_Sapphire                = 2697
    VivoActive_3                    = 2700
    Edge_1030                       = 2713
    ForeRunner_35_Sea               = 2727
    ForeRunner_235_China_NFC        = 2733
    Foretrex_601_701                = 2769
    VivoMove_HR                     = 2772
    Vector_3                        = 2787
    Fenix_5_Asia                    = 2796
    Fenix_5s_Asia                   = 2797
    Fenix_5x_Asia                   = 2798
    Approach_z80                    = 2806
    ForeRunner_35_Korea             = 2814
    D2Charlie                       = 2819
    VivoSmart3_Apac                 = 2831
    VivoSport_Apac                  = 2832
    ForeRunner_935_Asia             = 2833
    Descent                         = 2859
    VivoFit_4                       = 2878
    Forerunner_645                  = 2886
    Forerunner_645m                 = 2888
    ForeRunner_30                   = 2891
    Fenix_5S_Plus                   = 2900
    Edge_130                        = 2909
    Edge_1030_Asia                  = 2924
    Vivosmart_4                     = 2927
    VivoMove_HR_Asia                = 2945
    GPS_2957                        = 2957
    Approach_x10                    = 2962
    ForeRunner_30_Asia              = 2977
    VivoActive_3m_w                 = 2988
    ForeRunner_645_Asia             = 3003
    ForeRunner_645M_Asia            = 3004
    Edge_Explore                    = 3011
    GPSMap66                        = 3028
    Approach_S10                    = 3049
    VivoActive_3M_l                 = 3066
    Approach_G80                    = 3085
    Edge_130_Asia                   = 3092
    Edge_1030_Bontrager             = 3095
    GPS_3107                        = 3107
    Fenix_5_Plus                    = 3110
    Fenix_5x_Plus                   = 3111
    Edge_520_Plus                   = 3112
    ForeRunner_945                  = 3113
    Edge_530                        = 3121
    Edge_830                        = 3122
    Instinct_Esports                = 3126
    Fenix_5S_Plus_Apac              = 3134
    Fenix_5X_Plus_Apac              = 3135
    Edge_520_Plus_Apac              = 3142
    Descent_t1                      = 3143
    Forerunner235L_Asia             = 3144
    Forerunner235_Asia              = 3145
    VivoActive_3m_Asia              = 3163
    Bike_Speed_Sensor_Gen3          = 3192
    Bike_Cadence_Sensor_Gen3        = 3193
    VivoSmart_4_Asia                = 3218
    VivoActive_4_Small              = 3224
    VivoActive_4_Large              = 3225
    Venu                            = 3226
    Marq_Driver                     = 3246
    Marq_Aviator                    = 3247
    Marq_Captain                    = 3248
    Marq_Commander                  = 3249
    Marq_Expedition                 = 3250
    Marq_Athlete                    = 3251
    Descent_Mk2                     = 3258
    GPSMap_66i                      = 3284
    Fenix_6S_Sport                  = 3287
    Fenix_6S_Pro                    = 3288
    Fenix_6_Sport                   = 3289
    Fenix_6                         = 3290
    Fenix_6X                        = 3291
    Sensor_Hub_3294                 = 3294
    HRM_Dual                        = 3299
    HRM_Pro                         = 3300
    VivoMove_3_Premium              = 3308
    Approach_S40                    = 3314
    ForeRunner_245M_Asia            = 3321
    Edge_530_Apac                   = 3349
    Edge_830_Apac                   = 3350
    VivoMove_3                      = 3378
    VivoActive_4_Small_Asia         = 3387
    VivoActive_4_Large_Asia         = 3388
    VivoActive_4_OLED_Asia          = 3389
    SWIM2                           = 3405
    Marq_Driver_Asia                = 3420
    Marq_Aviator_Asia               = 3421
    VivoMove_3_Asia                 = 3422
    ForeRunner_945_Asia             = 3441
    VivoActive_3T_CHN               = 3446
    Marq_Captain_Asia               = 3448
    Marq_Commander_Asia             = 3449
    Marq_Expedition_Asia            = 3450
    Marq_Athlete_Asia               = 3451
    Instinct_Solar                  = 3466
    ForeRunner_45_Asia              = 3469
    VivoActive_3_Daimler            = 3473
    legacy_Rey                      = 3498
    Legacy_Darth_Vader              = 3499
    Legacy_Captain_Marvel           = 3500
    Legacy_First_Avenger            = 3501
    Fenix_6S_Sport_Asia             = 3512
    Fenix_6S_Asia                   = 3513
    Fenix_6_Sport_Asia              = 3514
    Fenix_6_Asia                    = 3515
    Fenix_6X_Asia                   = 3516
    Legacy_Captain_Marvel_Asia      = 3535
    Legacy_First_Avenger_Asia       = 3536
    Legacy_Rey_Asia                 = 3537
    Legacy_Darth_Vader_Asia         = 3538
    Descent_mk2s                    = 3542
    ForeRunner_945_LTE              = 3652
    Edge_130_Plus                   = 3558
    Edge_1030_Plus                  = 3570
    Rally_200                       = 3578
    ForeRunner_745                  = 3589
    VenusQ                          = 3600
    Lily                            = 3615
    Marq_Adventurer                 = 3624
    Enduro                          = 3638
    Marq_Adventurer_Asia            = 3648
    SWIM2_Apac                      = 3639
    Descent_Mk2_Asia                = 3702  # Mk2 and Mk2i
    Venu_2                          = 3703
    Venu_2s                         = 3704
    Venu_Daimler_Asia               = 3737
    Marq_Golfer                     = 3739
    Venu_Daimler                    = 3740
    ForeRunner_745_Asia             = 3794
    Lily_Asia                       = 3809
    Edge_1030_Plus_Asia             = 3812
    Edge_130_Plus_Asia              = 3813
    Approach_S12                    = 3823
    VenusQ_Asia                     = 3837
    Edge_1040                       = 3843
    Marq_Golfer_Asia                = 3850
    Venu_2_Plus                     = 3851
    gnss                            = 3865
    ForeRunner_55                   = 3869
    Enduro_Asia                     = 3872
    INSTINCT_2                      = 3888
    Fenix_7S                        = 3905
    Fenix_7                         = 3906
    Fenix_7X                        = 3907
    Fenix_7S_APAC                   = 3908
    Fenix_7_APAC                    = 3909
    Fenix_X_APAC                    = 3910
    Approach_G12                    = 3927
    Descent_Mk2s_Asia               = 3930
    Approach_S42                    = 3934
    Epix_gen2                       = 3943
    Epix_gen2_apac                  = 3944
    Venu_2S_Asia                    = 3949
    Venu_2_Asia                     = 3950
    ForeRunner_945_LTE_Asia         = 3978
    VivoMove_Sport                  = 3982
    VivoMove_Trend                  = 3983
    Approach_S12_Asia               = 3986
    ForeRunner_255_Music            = 3990
    ForeRunner_255_Small_Music      = 3991
    ForeRunner_255                  = 3992
    ForeRunner_255_Small            = 3993
    Approach_G12_Asia               = 4001
    Approach_S42_Asia               = 4002
    Descent_g1                      = 4005
    Venu2_Plus_Asia                 = 4017
    ForeRunner_955                  = 4024
    ForeRunner_55_Asia              = 4033
    EDGE_540                        = 4061
    EDGE_840                        = 4062
    VivoSmart_5                     = 4063
    INSTINCT_2_ASIA                 = 4071
    MARQ_GEN2                       = 4105  # Adventurer, Athlete, Captain, Golfer
    VENUSQ2                         = 4115
    VENUSQ2MUSIC                    = 4116
    MARQ_GEN2_AVIATOR               = 4124
    D2_AIR_X10                      = 4125
    HRM_PRO_PLUS                    = 4130
    DESCENT_G1_ASIA                 = 4132
    TACTIX7                         = 4135
    INSTINCT_CROSSOVER              = 4155
    EDGE_EXPLORE2                   = 4169
    APPROACH_S70                    = 4233
    FR265_LARGE                     = 4257
    FR265_SMALL                     = 4258
    TACX_NEO_SMART                  = 4265  # Neo Smart, Tacx
    TACX_NEO2_SMART                 = 4266  # Neo 2 Smart, Tacx
    TACX_NEO2_T_SMART               = 4267  # Neo 2T Smart, Tacx
    TACX_NEO_SMART_BIKE             = 4268  # Neo Smart Bike, Tacx
    TACX_SATORI_SMART               = 4269  # Satori Smart, Tacx
    TACX_FLOW_SMART                 = 4270  # Flow Smart, Tacx
    TACX_VORTEX_SMART               = 4271  # Vortex Smart, Tacx
    TACX_BUSHIDO_SMART              = 4272  # Bushido Smart, Tacx
    TACX_GENIUS_SMART               = 4273  # Genius Smart, Tacx
    TACX_FLUX_FLUX_S_SMART          = 4274  # Flux/Flux S Smart, Tacx
    TACX_FLUX2_SMART                = 4275  # Flux 2 Smart, Tacx
    TACX_MAGNUM                     = 4276  # Magnum, Tacx
    EDGE_1040_ASIA                  = 4305
    EPIX_GEN2_PRO_42                = 4312
    EPIX_GEN2_PRO_47                = 4313
    EPIX_GEN2_PRO_51                = 4314
    ForeRunner_965                  = 4315
    ENDURO2                         = 4341
    Fenix_7_PRO_SOLAR               = 4375
    INSTINCT_2X                     = 4394
    DESCENT_T2                      = 4442
    #
    FootPod_SDM4                    = 10007
    Edge_Remote                     = 10014
    Training_Center                 = 20119
    TACX_Training_App_Win           = 20533
    TACX_Training_App_Mac           = 20534
    TACX_Training_App_Mac_Catalyst  = 20565
    TACX_Training_App_Android       = 30045
    TACX_Training_Aapp_IOS          = 30046
    TACX_Training_App_Legacy        = 30047
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
    Accelerometer_865               = 865
    Accelerometer_901               = 901
    GPS_1619                        = 1619
    GPS_1620                        = 1620
    GPS_1621                        = 1621
    GPS_2957                        = 2957
    Accelerometer_8194              = 8194
    Accelerometer_8191              = 8191
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
    Accelerometer_49208             = 49208
    invalid                         = 65535


class WahooFitnessProduct(FuzzyFieldEnum):
    """Wahoo Fitness product codes used in FIT files."""

    RPM_Sensor = 6


class ScoscheProduct(FuzzyFieldEnum):
    """Scosche product codes used in FIT files."""

    Rhythm_Plus_Armband_HRM = 2


class HealthAndLifeProduct(FuzzyFieldEnum):
    """Scosche product codes used in FIT files."""

    Accelerometer_515 = 515


class XplovaProduct(FuzzyFieldEnum):
    """Scosche product codes used in FIT files."""

    bluetooth_low_energy_chipset_11 = 11


class FaveroProduct(FuzzyFieldEnum):
    """Scosche product codes used in FIT files."""

    ASSIOMA_UNO     = 10
    ASSIOMA_DUO     = 12


class UnknownProduct(UnknownEnumValue):
    """Unknown product codes used in FIT files."""


def product_enum(manufacturer, product_str):
    """Return a product enum given the manufacturer enum and a product string."""
    _manufacturer_to_product_enum = {
        Manufacturer.Garmin                 : GarminProduct,
        Manufacturer.Garmin_local           : GarminLocalProduct,
        Manufacturer.Dynastream             : GarminProduct,
        Manufacturer.Dynastream_OEM         : GarminProduct,
        Manufacturer.Wahoo_Fitness          : WahooFitnessProduct,
        Manufacturer.Scosche                : ScoscheProduct,
        Manufacturer.Health_and_Life        : HealthAndLifeProduct,
        Manufacturer.Xplova                 : XplovaProduct,
        Manufacturer.favero_electronics     : FaveroProduct,
        Manufacturer.invalid                : GarminProduct,
    }
    return _manufacturer_to_product_enum[manufacturer].from_string(product_str)
