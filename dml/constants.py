class MathematicalConstants:
    """Mathematical constants"""
    PI = 3.141592653589793
    E = 2.718281828459045
    PHI = 1.618033988749894
    EULER_MASCHERONI = 0.577215664901532
    IMAGINARY_UNIT = 1j
    
    # Number Theory
    APERY = 1.20205690315959428539
    CATALAN = 0.91596559417721901505
    GLAISHER_KINKELIN = 1.28242712910062263687
    KHINCHIN = 2.68545200106530644530
    MILL = 1.30637788386308069046
    RAMANUJAN_SOLDNER = 1.45136923488338105028
    
    # Geometric
    SQRT2 = 1.41421356237309504880
    SQRT3 = 1.73205080756887729352
    SQRT5 = 2.23606797749978969641
    CUBE_ROOT2 = 1.25992104989487316476
    CUBE_ROOT3 = 1.44224957030740838232
    SILVER_RATIO = 2.41421356237309504880
    BRONZE_RATIO = 3.30277563773199464656
    
    # Analysis
    FEIGENBAUM_ALPHA = 2.50290787509589282228
    FEIGENBAUM_DELTA = 4.66920160910299067185
    LEVY = 3.27582291872181115978
    OMEGA = 0.56714329040978387299
    CONWAY = 1.30357726903429639125
    PARIS = 1.09864196439415648573
    
    # Probability
    GAUSS = 0.83462684167407318628
    ERDOS_BORWEIN = 1.60669515241529176378
    COPELAND_ERDOS = 0.23571113171923293137
    CHAMPERNOWNE = 0.12345678910111213141
    
    # Special Functions
    GAMMA_1_4 = 3.62560990822290831193
    GAMMA_1_3 = 2.67893853470774763365
    GAMMA_1_2 = 1.77245385090551602729
    BETA_1_4 = 5.24411510858423962093
    
    # Computational
    MACHINE_EPSILON = 2.220446049250313e-16
    MAX_FLOAT = 1.7976931348623157e+308
    MIN_FLOAT = 2.2250738585072014e-308
    MAX_64INT = 2**64 - 1


class LengthConstants:
    """Length constants (meter base)"""
    # Metric
    METER = 1.0
    KILOMETER = 1000.0
    HECTOMETER = 100.0
    DECAMETER = 10.0
    DECIMETER = 0.1
    CENTIMETER = 0.01
    MILLIMETER = 0.001
    MICROMETER = 1e-6
    NANOMETER = 1e-9
    PICOMETER = 1e-12
    FEMTOMETER = 1e-15
    
    # Imperial
    INCH = 0.0254
    FOOT = 0.3048
    YARD = 0.9144
    MILE = 1609.344
    THOU = 0.0000254
    HAND = 0.1016
    LINK = 0.201168
    ROD = 5.0292
    CHAIN = 20.1168
    FURLONG = 201.168
    
    # British Imperial
    BRITISH_INCH = 0.025399977
    BRITISH_FOOT = 0.304799724
    BRITISH_YARD = 0.914399172
    BRITISH_MILE = 1609.3426
    NAUTICAL_MILE = 1852.0
    
    # Asian
    SUN = 0.030303
    SHAKU = 0.30303
    KEN = 1.81818
    RI = 3927.27
    LI = 500.0
    CHI = 0.3333
    ZHANG = 3.3333
    HAATH = 0.4572
    GAZ = 0.9144
    KOS = 3657.6
    
    # Arabic
    QABDH = 0.066667
    DIRAA = 0.66667
    FARSKH = 5970.0
    
    # Persian
    GEREEH = 0.0566
    QABZEH = 0.2264
    BAA = 1.132
    ARESH = 1.7
    FARSANG = 6240.0
    PARASANG = 6240.0
    
    # Astronomical
    ASTRONOMICAL_UNIT = 1.495978707e11
    LIGHT_YEAR = 9.4607304725808e15
    PARSEC = 3.0856775814913673e16
    LIGHT_SECOND = 299792458.0
    LIGHT_SPEED = 299792458
    LIGHT_MINUTE = 1.798754748e10
    LIGHT_HOUR = 1.0792528488e12
    ANGSTROM = 1e-10


class AreaConstants:
    """Area constants (square meter base)"""
    # Metric
    SQUARE_METER = 1.0
    SQUARE_KILOMETER = 1e6
    SQUARE_HECTOMETER = 1e4
    SQUARE_DECAMETER = 100.0
    SQUARE_DECIMETER = 0.01
    SQUARE_CENTIMETER = 1e-4
    SQUARE_MILLIMETER = 1e-6
    HECTARE = 10000.0
    ARE = 100.0
    
    # Imperial
    SQUARE_INCH = 0.00064516
    SQUARE_FOOT = 0.09290304
    SQUARE_YARD = 0.83612736
    SQUARE_MILE = 2589988.110336
    ACRE = 4046.8564224
    ROOD = 1011.7141056
    PERCH = 25.29285264
    
    # Asian
    TSUB0 = 3.305785  # Japanese
    SE = 99.17355     # Japanese
    TAN = 991.7355    # Japanese
    CH0 = 9917.355    # Japanese
    
    # Agricultural
    BIGHA = 1600.0    # Indian
    KATHA = 66.89     # Indian
    KANAL = 505.857   # Pakistani
    
    # Astronomical
    SQUARE_ASTRONOMICAL_UNIT = 2.237952e22
    SQUARE_LIGHT_YEAR = 8.950542e31
    SQUARE_PARSEC = 9.521409e32


class VolumeConstants:
    """Volume constants (cubic meter base)"""
    # Metric
    CUBIC_METER = 1.0
    CUBIC_KILOMETER = 1e9
    CUBIC_DECIMETER = 0.001
    CUBIC_CENTIMETER = 1e-6
    CUBIC_MILLIMETER = 1e-9
    LITER = 0.001
    MILLILITER = 1e-6
    MICROLITER = 1e-9
    
    # Imperial
    CUBIC_INCH = 1.6387064e-5
    CUBIC_FOOT = 0.028316846592
    CUBIC_YARD = 0.764554857984
    CUBIC_MILE = 4.168181825440579e9
    GALLON_US = 0.003785411784
    GALLON_UK = 0.00454609
    QUART_US = 0.000946352946
    QUART_UK = 0.0011365225
    PINT_US = 0.000473176473
    PINT_UK = 0.00056826125
    FLUID_OUNCE_US = 2.95735295625e-5
    FLUID_OUNCE_UK = 2.84130625e-5
    
    # Cooking
    TEASPOON = 4.92892159375e-6
    TABLESPOON = 1.478676478125e-5
    CUP = 0.0002365882365
    
    # Asian
    SH0 = 0.00180391  # Japanese
    G0 = 0.180391     # Japanese
    TO = 0.0180391    # Japanese
    KOKU = 0.180391   # Japanese
    
    # Astronomical
    CUBIC_ASTRONOMICAL_UNIT = 3.347e33
    CUBIC_LIGHT_YEAR = 8.467e47
    CUBIC_PARSEC = 2.938e49


class MassConstants:
    """Mass constants (kilogram base)"""
    KILOGRAM = 1.0
    GRAM = 0.001
    MILLIGRAM = 1e-6
    MICROGRAM = 1e-9
    TONNE = 1000.0
    KILOTONNE = 1e6
    MEGATONNE = 1e9
    
    # Imperial
    POUND = 0.45359237
    OUNCE = 0.028349523125
    STONE = 6.35029318
    SHORT_TON = 907.18474
    LONG_TON = 1016.0469088
    
    # Particles
    ELECTRON_MASS = 9.1093837015e-31
    PROTON_MASS = 1.67262192369e-27
    NEUTRON_MASS = 1.67492749804e-27
    MUON_MASS = 1.883531627e-28
    TAU_MASS = 3.16754e-27
    
    # Astronomical
    SUN_MASS = 1.989e30
    EARTH_MASS = 5.9722e24
    MOON_MASS = 7.342e22
    JUPITER_MASS = 1.898e27
    MILKY_WAY_MASS = 1.5e42
    ANDROMEDA_MASS = 1.5e42
    
    # Atomic
    ATOMIC_MASS_UNIT = 1.66053906660e-27
    DALTON = 1.66053906660e-27
    AVOGADRO_CONSTANT = 6.02214076e23
    HYDROGEN_MASS = 1.6735575e-27
    CARBON_12_MASS = 1.992646879e-26
    OXYGEN_MASS = 2.656696e-26


class TemperatureConstants:
    """Temperature constants (kelvin base)"""
    KELVIN = 1.0
    CELSIUS_OFFSET = 273.15
    FAHRENHEIT_SCALE = 5.0/9.0
    FAHRENHEIT_OFFSET = 459.67
    RANKINE_SCALE = 5.0/9.0
    
    # Absolute Zero Points
    ABSOLUTE_ZERO_K = 0.0
    ABSOLUTE_ZERO_C = -273.15
    ABSOLUTE_ZERO_F = -459.67
    ABSOLUTE_ZERO_R = 0.0
    
    # Important Temperatures
    ROOM_TEMPERATURE = 298.15  # 25°C
    HUMAN_BODY_TEMP = 310.15   # 37°C
    WATER_FREEZING = 273.15    # 0°C
    WATER_BOILING = 373.15     # 100°C
    
    # Scientific
    PLANCK_TEMPERATURE = 1.416784e32
    HAWKING_TEMPERATURE = 1.227e23


class TimeConstants:
    """Time constants (second base)"""
    SECOND = 1.0
    MILLISECOND = 0.001
    MICROSECOND = 1e-6
    NANOSECOND = 1e-9
    PICOSECOND = 1e-12
    FEMTOSECOND = 1e-15
    
    MINUTE = 60.0
    HOUR = 3600.0
    DAY = 86400.0
    WEEK = 604800.0
    MONTH = 2629746.0  # average
    YEAR = 31556952.0  # solar year
    DECADE = 315569520.0
    CENTURY = 3155695200.0
    MILLENNIUM = 31556952000.0
    
    # Astronomical
    SIDEREAL_DAY = 86164.0905
    SIDEREAL_YEAR = 31558149.54
    TROPICAL_YEAR = 31556925.2
    
    # Scientific
    PLANCK_TIME = 5.391247e-44


class SpeedConstants:
    """Speed constants (m/s base)"""
    METER_PER_SECOND = 1.0
    KILOMETER_PER_HOUR = 0.2777777778
    MILE_PER_HOUR = 0.44704
    KNOT = 0.514444
    FOOT_PER_SECOND = 0.3048
    MACH = 340.3  # at sea level
    LIGHT_SPEED_VACUUM = 299792458.0


class PressureConstants:
    """Pressure constants (pascal base)"""
    PASCAL = 1.0
    KILOPASCAL = 1000.0
    MEGAPASCAL = 1e6
    GIGAPASCAL = 1e9
    BAR = 100000.0
    MILLIBAR = 100.0
    ATMOSPHERE = 101325.0
    TORR = 133.322
    MMHG = 133.322
    PSI = 6894.76
    INHG = 3386.39


class EnergyConstants:
    """Energy constants (joule base)"""
    JOULE = 1.0
    KILOJOULE = 1000.0
    MEGAJOULE = 1e6
    GIGAJOULE = 1e9
    CALORIE = 4.184
    KILOCALORIE = 4184.0
    ELECTRONVOLT = 1.602176634e-19
    KILOELECTRONVOLT = 1.602176634e-16
    MEGAELECTRONVOLT = 1.602176634e-13
    BRITISH_THERMAL_UNIT = 1055.05585262
    KILOWATT_HOUR = 3.6e6


class PowerConstants:
    """Power constants (watt base)"""
    WATT = 1.0
    KILOWATT = 1000.0
    MEGAWATT = 1e6
    GIGAWATT = 1e9
    HORSEPOWER = 745.699872
    FOOT_POUND_PER_SECOND = 1.35581795


class AngleConstants:
    """Angle constants (radian base)"""
    RADIAN = 1.0
    DEGREE = 0.017453292519943295
    ARCMINUTE = 0.0002908882086657216
    ARCSECOND = 4.84813681109536e-6
    GRADIAN = 0.015707963267948967
    REVOLUTION = 6.283185307179586


class FrequencyConstants:
    """Frequency constants (hertz base)"""
    HERTZ = 1.0
    KILOHERTZ = 1000.0
    MEGAHERTZ = 1e6
    GIGAHERTZ = 1e9
    TERAHERTZ = 1e12
    RPM = 0.016666666666666666  # revolutions per minute


class DataStorageConstants:
    """Data storage constants (byte base)"""
    BYTE = 1.0
    KILOBYTE = 1024.0
    MEGABYTE = 1048576.0
    GIGABYTE = 1073741824.0
    TERABYTE = 1099511627776.0
    PETABYTE = 1125899906842624.0


class ElectricalConstants:
    """Electrical constants"""
    # Resistance (ohm base)
    OHM = 1.0
    KILOOHM = 1000.0
    MEGAOHM = 1e6
    
    # Voltage (volt base)
    VOLT = 1.0
    KILOVOLT = 1000.0
    MEGAVOLT = 1e6
    
    # Current (ampere base)
    AMPERE = 1.0
    MILLIAMPERE = 0.001
    MICROAMPERE = 1e-6
    
    # Capacitance (farad base)
    FARAD = 1.0
    MICROFARAD = 1e-6
    NANOFARAD = 1e-9
    PICOFARAD = 1e-12
    
    # Inductance (henry base)
    HENRY = 1.0
    MILLIHENRY = 0.001
    MICROHENRY = 1e-6


class ChemicalConstants:
    """Chemical constants"""
    # Amount of substance (mole base)
    MOLE = 1.0
    MILLIMOLE = 0.001
    KILOMOLE = 1000.0
    
    # Concentration (molar base)
    MOLAR = 1.0
    MILLIMOLAR = 0.001
    MICROMOLAR = 1e-6
    NANOMOLAR = 1e-9
    
    # Gas constant
    GAS_CONSTANT = 8.314462618  # J/mol·K
    BOLTZMANN_CONSTANT = 1.380649e-23  # J/K


class NuclearConstants:
    """Nuclear constants"""
    BECQUEREL = 1.0  # decays per second
    CURIE = 3.7e10
    RUTHERFORD = 1e6
    GRAY = 1.0  # absorbed dose
    SIEVERT = 1.0  # equivalent dose


class CosmologicalConstants:
    """Cosmological constants"""
    HUBBLE_CONSTANT = 2.25e-18  # 1/s
    CRITICAL_DENSITY = 9.47e-27  # kg/m³
    COSMIC_MICROWAVE_BACKGROUND_TEMP = 2.725  # K
    DARK_ENERGY_DENSITY = 6.91e-10  # J/m³


class GravitationalConstants:
    """Gravitational constants"""
    GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³/kg·s²
    STANDARD_GRAVITY = 9.80665  # m/s²
    ESCAPE_VELOCITY_EARTH = 11186.0  # m/s
    SOLAR_MASS_PARAMETER = 1.32712440018e20  # m³/s²


class QuantumConstants:
    """Quantum constants"""
    PLANCK_CONSTANT = 6.62607015e-34  # J·s
    REDUCED_PLANCK_CONSTANT = 1.054571817e-34  # J·s
    BOHR_MAGNETON = 9.2740100783e-24  # J/T
    NUCLEAR_MAGNETON = 5.0507837461e-27  # J/T
    BOHR_RADIUS = 5.29177210903e-11  # m
    RYDBERG_CONSTANT = 10973731.568160  # 1/m


class ElectromagneticConstants:
    """Electromagnetic constants"""
    VACUUM_PERMEABILITY = 1.25663706212e-6  # N/A²
    VACUUM_PERMITTIVITY = 8.8541878128e-12  # F/m
    COULOMB_CONSTANT = 8.9875517873681764e9  # N·m²/C²
    ELEMENTARY_CHARGE = 1.602176634e-19  # C
    ELECTRON_MAGNETIC_MOMENT = 9.2847647043e-24  # J/T
    PROTON_MAGNETIC_MOMENT = 1.41060679736e-26  # J/T


class ThermodynamicConstants:
    """Thermodynamic constants"""
    STEFAN_BOLTZMANN_CONSTANT = 5.670374419e-8  # W/m²·K⁴
    WIEN_DISPLACEMENT_CONSTANT = 0.002897771955  # m·K
    FIRST_RADIATION_CONSTANT = 3.741771852e-16  # W·m²
    SECOND_RADIATION_CONSTANT = 0.01438776977  # m·K


class OpticalConstants:
    """Optical constants"""
    SPEED_OF_LIGHT = 299792458.0  # m/s
    REFRACTIVE_INDEX_AIR = 1.000293
    REFRACTIVE_INDEX_WATER = 1.333
    REFRACTIVE_INDEX_GLASS = 1.52
    ABBE_NUMBER = 45.0  # for typical glass


class AcousticConstants:
    """Acoustic constants"""
    SPEED_OF_SOUND_AIR = 343.0  # m/s at 20°C
    SPEED_OF_SOUND_WATER = 1480.0  # m/s
    SPEED_OF_SOUND_STEEL = 5960.0  # m/s
    REFERENCE_SOUND_PRESSURE = 2e-5  # Pa
    REFERENCE_SOUND_INTENSITY = 1e-12  # W/m²


class MaterialConstants:
    """Material constants"""
    YOUNGS_MODULUS_STEEL = 2.0e11  # Pa
    YOUNGS_MODULUS_ALUMINUM = 7.0e10  # Pa
    YOUNGS_MODULUS_COPPER = 1.1e11  # Pa
    SHEAR_MODULUS_STEEL = 7.9e10  # Pa
    BULK_MODULUS_WATER = 2.2e9  # Pa


class FinancialConstants:
    """Financial constants"""
    # (Example values - these vary by country and time)
    ANNUAL_INTEREST_RATE = 0.05
    MONTHLY_INTEREST_RATE = 0.0041667
    INFLATION_RATE = 0.02
    TAX_RATE = 0.20
    EXCHANGE_RATE_USD_EUR = 0.85  # example


class GeographicalConstants:
    """Geographical constants"""
    EARTH_RADIUS_EQUATORIAL = 6378137.0  # m
    EARTH_RADIUS_POLAR = 6356752.0  # m
    EARTH_RADIUS_MEAN = 6371000.0  # m
    EARTH_MASS = 5.9722e24  # kg
    EARTH_VOLUME = 1.08321e21  # m³
    EARTH_SURFACE_AREA = 5.10072e14  # m²


class BiologicalConstants:
    """Biological constants"""
    AVERAGE_HUMAN_HEIGHT = 1.7  # m
    AVERAGE_HUMAN_WEIGHT = 62.0  # kg
    AVERAGE_HUMAN_BODY_TEMP = 310.15  # K
    AVERAGE_HUMAN_HEART_RATE = 72.0  # bpm
    AVERAGE_HUMAN_BLOOD_PRESSURE = 12000.0  # Pa (systolic)


class EngineeringConstants:
    """Engineering constants"""
    STANDARD_ATMOSPHERE = 101325.0  # Pa
    STANDARD_TEMPERATURE = 293.15  # K
    STANDARD_PRESSURE = 101325.0  # Pa
    GRAVITY_ENGINEERING = 9.80665  # m/s²


class ConversionFactors:
    """Conversion factors"""
    # Common conversion factors
    DEGREE_TO_RADIAN = 3.141592653589793 / 180.0
    RADIAN_TO_DEGREE = 180.0 / 3.141592653589793
    INCH_TO_CM = 2.54
    CM_TO_INCH = 0.393700787
    POUND_TO_KG = 0.45359237
    KG_TO_POUND = 2.20462262
    GALLON_TO_LITER = 3.78541178
    LITER_TO_GALLON = 0.264172052
    
    # Mathematical Conversion Factors
    DEGREES_TO_RADIANS = 3.141592653589793 / 180.0
    RADIANS_TO_DEGREES = 180.0 / 3.141592653589793
    GRADIANS_TO_DEGREES = 0.9
    DEGREES_TO_GRADIANS = 1.1111111111111112
    
    # Physical Conversion Factors
    ELECTRONVOLT_TO_JOULE = 1.602176634e-19
    JOULE_TO_ELECTRONVOLT = 6.241509074e18
    CALORIE_TO_JOULE = 4.184
    JOULE_TO_CALORIE = 0.239005736
    BTU_TO_JOULE = 1055.05585262
    JOULE_TO_BTU = 9.478171203e-4
    
    # Astronomical Conversion Factors
    LIGHTYEAR_TO_PARSEC = 0.306601
    PARSEC_TO_LIGHTYEAR = 3.26156
    ASTRONOMICALUNIT_TO_LIGHTYEAR = 1.58125e-5
    LIGHTYEAR_TO_ASTRONOMICALUNIT = 63241.1
    
    # Time Conversion Factors
    SECONDS_TO_MINUTES = 1.0 / 60.0
    MINUTES_TO_HOURS = 1.0 / 60.0
    HOURS_TO_DAYS = 1.0 / 24.0
    DAYS_TO_WEEKS = 1.0 / 7.0
    WEEKS_TO_YEARS = 1.0 / 52.1775
    YEARS_TO_CENTURIES = 1.0 / 100.0


class AdditionalConstants:
    """Additional useful constants"""
    GOLDEN_ANGLE = 137.50776405003785
    SILVER_CONSTANT = 3.35988566624317755317201130291892717968890513373
    PLASTIC_CONSTANT = 1.32471795724474602596090885447809734073440405690
    UNIVERSAL_PARABOLIC_CONSTANT = 2.29558714939263807403429804918949038759783220342


class SIUnits:
    """SI Units definitions"""
    LENGTH = "Meter"
    MASS = "Kilogram"
    TIME = "Secend"
    ELECTRIC_CURRENT = "Amper"
    TEMPERATURE = "Kelvin"
    CHEMICAL = "Mole"
    LUMINOUS_INTENSITY = "Candela"
    SPEED = "Meter per secend"