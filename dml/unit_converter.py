class TemperatureConverter:
    ABSOLUTE_ZERO = {
        'K': 0,
        'C': -273.15,
        'F': -459.67,
        'R': 0,
        'De': 559.725,
        'N': -90.1395,
        'Re': -218.52,
        'Ro': -135.90
    }
    
    @staticmethod
    def absolute_zero(unit='K'):
        return TemperatureConverter.ABSOLUTE_ZERO.get(unit.upper(), 0)
    
    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15
    
    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    
    @staticmethod
    def fahrenheit_to_kelvin(f):
        return (f + 459.67) * 5/9
    
    @staticmethod
    def kelvin_to_fahrenheit(k):
        return (k * 9/5) - 459.67
    
    @staticmethod
    def rankine_to_celsius(r):
        return (r - 491.67) * 5/9
    
    @staticmethod
    def celsius_to_rankine(c):
        return (c + 273.15) * 9/5
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        if from_unit == 'K':
            kelvin = value
        elif from_unit == 'C':
            kelvin = TemperatureConverter.celsius_to_kelvin(value)
        elif from_unit == 'F':
            kelvin = TemperatureConverter.fahrenheit_to_kelvin(value)
        elif from_unit == 'R':
            kelvin = value * 5/9
        else:
            raise ValueError(f"unknown unit : {from_unit}")
        
        if to_unit == 'K':
            return kelvin
        elif to_unit == 'C':
            return TemperatureConverter.kelvin_to_celsius(kelvin)
        elif to_unit == 'F':
            return TemperatureConverter.kelvin_to_fahrenheit(kelvin)
        elif to_unit == 'R':
            return kelvin * 9/5
        else:
            raise ValueError(f"unknown unit : {to_unit}")


class LengthConverter:
    TO_METER = {
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'inch': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34,
        'nmi': 1852.0,
        'au': 1.496e11,
        'ly': 9.461e15,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in LengthConverter.TO_METER:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in LengthConverter.TO_METER:
            raise ValueError(f"unknown unit : {to_unit}")
        
        meters = value * LengthConverter.TO_METER[from_unit]
        return meters / LengthConverter.TO_METER[to_unit]
    

    @staticmethod
    def inch_to_centimeter(inch):
        return inch * 2.54
    
    @staticmethod
    def centimeter_to_inch(cm):
        return cm / 2.54
    
    @staticmethod
    def foot_to_meter(ft):
        return ft * 0.3048
    
    @staticmethod
    def meter_to_foot(m):
        return m / 0.3048
    
    @staticmethod
    def yard_to_meter(yd):
        return yd * 0.9144
    
    @staticmethod
    def meter_to_yard(m):
        return m / 0.9144
    
    @staticmethod
    def mile_to_kilometer(mi):
        return mi * 1.60934
    
    @staticmethod
    def kilometer_to_mile(km):
        return km / 1.60934


class AreaConverter:
    TO_SQUARE_METER = {
        'm²': 1.0,
        'cm²': 0.0001,
        'mm²': 1e-6,
        'km²': 1e6,
        'ha': 10000.0,
        'acre': 4046.86,
        'ft²': 0.092903,
        'yd²': 0.836127,
        'mi²': 2.59e6,
        'in²': 0.00064516,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in AreaConverter.TO_SQUARE_METER:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in AreaConverter.TO_SQUARE_METER:
            raise ValueError(f"unknown unit : {to_unit}")
        
        square_meters = value * AreaConverter.TO_SQUARE_METER[from_unit]
        return square_meters / AreaConverter.TO_SQUARE_METER[to_unit]


    @staticmethod
    def square_meter_to_hectare(m2):
        return m2 / 10000
    
    @staticmethod
    def acre_to_square_meter(ac):
        return ac * 4046.86
    
    @staticmethod
    def square_meter_to_acre(m2):
        return m2 / 4046.86
    
    @staticmethod
    def square_inch_to_square_centimeter(in2):
        return in2 * 6.4516
    
    @staticmethod
    def square_centimeter_to_square_inch(cm2):
        return cm2 / 6.4516
    
    @staticmethod
    def square_foot_to_square_meter(ft2):
        return ft2 * 0.092903
    
    @staticmethod
    def square_meter_to_square_foot(m2):
        return m2 / 0.092903


class VolumeConverter:
    TO_CUBIC_METER = {
        'm³': 1.0,
        'l': 0.001,
        'ml': 1e-6,
        'cm³': 1e-6,
        'ft³': 0.0283168,
        'in³': 1.6387e-5,
        'yd³': 0.764555,
        'gal': 0.00378541,
        'gal_uk': 0.00454609,
        'fl_oz': 2.95735e-5,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in VolumeConverter.TO_CUBIC_METER:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in VolumeConverter.TO_CUBIC_METER:
            raise ValueError(f"unknown unit : {to_unit}")

        cubic_meters = value * VolumeConverter.TO_CUBIC_METER[from_unit]
        return cubic_meters / VolumeConverter.TO_CUBIC_METER[to_unit]
    

    @staticmethod
    def liter_to_milliliter(l):
        return l * 1000
    
    @staticmethod
    def milliliter_to_liter(ml):
        return ml / 1000
    
    @staticmethod
    def cubic_meter_to_liter(m3):
        return m3 * 1000
    
    @staticmethod
    def liter_to_cubic_meter(l):
        return l / 1000
    
    @staticmethod
    def gallon_to_liter(gal):
        return gal * 3.78541
    
    @staticmethod
    def liter_to_gallon(l):
        return l / 3.78541
    
    @staticmethod
    def cubic_inch_to_liter(in3):
        return in3 * 0.0163871
    
    @staticmethod
    def liter_to_cubic_inch(l):
        return l / 0.0163871
    
    @staticmethod
    def cubic_foot_to_liter(ft3):
        return ft3 * 28.3168
    
    @staticmethod
    def liter_to_cubic_foot(l):
        return l / 28.3168
    
    @staticmethod
    def fluid_ounce_to_milliliter(fl_oz):
        return fl_oz * 29.5735
    
    @staticmethod
    def milliliter_to_fluid_ounce(ml):
        return ml / 29.5735


class MassConverter:
    TO_KILOGRAM = {
        'kg': 1.0,
        'g': 0.001,
        'mg': 1e-6,
        'ton': 1000.0,
        'lb': 0.453592,
        'oz': 0.0283495,
        'st': 6.35029,
        'ct': 0.0002,
        't_uk': 1016.05,
        't_us': 907.185,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in MassConverter.TO_KILOGRAM:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in MassConverter.TO_KILOGRAM:
            raise ValueError(f"unknown unit : {to_unit}")

        kilograms = value * MassConverter.TO_KILOGRAM[from_unit]
        return kilograms / MassConverter.TO_KILOGRAM[to_unit]
    

    @staticmethod
    def kilogram_to_gram(kg):
        return kg * 1000
    
    @staticmethod
    def gram_to_kilogram(g):
        return g / 1000
    
    @staticmethod
    def gram_to_milligram(g):
        return g * 1000
    
    @staticmethod
    def milligram_to_gram(mg):
        return mg / 1000
    
    @staticmethod
    def pound_to_kilogram(lb):
        return lb * 0.453592
    
    @staticmethod
    def kilogram_to_pound(kg):
        return kg / 0.453592
    
    @staticmethod
    def ounce_to_gram(oz):
        return oz * 28.3495
    
    @staticmethod
    def gram_to_ounce(g):
        return g / 28.3495
    
    @staticmethod
    def ton_to_kilogram(ton):
        return ton * 1000
    
    @staticmethod
    def kilogram_to_ton(kg):
        return kg / 1000


class SpeedConverter:
    TO_METER_PER_SECOND = {
        'm/s': 1.0,
        'km/h': 0.277778,
        'mph': 0.44704,
        'kn': 0.514444,
        'ft/s': 0.3048,
        'c': 299792458.0,
        'mach': 340.3,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in SpeedConverter.TO_METER_PER_SECOND:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in SpeedConverter.TO_METER_PER_SECOND:
            raise ValueError(f"unknown unit : {to_unit}")

        mps = value * SpeedConverter.TO_METER_PER_SECOND[from_unit]
        return mps / SpeedConverter.TO_METER_PER_SECOND[to_unit]
    

    @staticmethod
    def kmh_to_ms(kmh):
        return kmh * 1000 / 3600
    
    @staticmethod
    def ms_to_kmh(ms):
        return ms * 3600 / 1000
    
    @staticmethod
    def mph_to_kmh(mph):
        return mph * 1.60934
    
    @staticmethod
    def kmh_to_mph(kmh):
        return kmh / 1.60934
    
    @staticmethod
    def knot_to_kmh(knot):
        return knot * 1.852
    
    @staticmethod
    def kmh_to_knot(kmh):
        return kmh / 1.852


class TimeConverter:
    TO_SECOND = {
        's': 1.0,
        'ms': 0.001,
        'μs': 1e-6,
        'ns': 1e-9,
        'min': 60.0,
        'h': 3600.0,
        'd': 86400.0,
        'wk': 604800.0,
        'mo': 2.62974e6,
        'yr': 3.15576e7,
        'dec': 3.15576e8,
        'cen': 3.15576e9,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in TimeConverter.TO_SECOND:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in TimeConverter.TO_SECOND:
            raise ValueError(f"unknown unit : {to_unit}")

        seconds = value * TimeConverter.TO_SECOND[from_unit]
        return seconds / TimeConverter.TO_SECOND[to_unit]
    

    @staticmethod
    def second_to_minute(s):
        return s / 60
    
    @staticmethod
    def minute_to_second(m):
        return m * 60
    
    @staticmethod
    def minute_to_hour(m):
        return m / 60
    
    @staticmethod
    def hour_to_minute(h):
        return h * 60
    
    @staticmethod
    def hour_to_second(h):
        return h * 3600
    
    @staticmethod
    def second_to_hour(s):
        return s / 3600
    
    @staticmethod
    def day_to_hour(d):
        return d * 24
    
    @staticmethod
    def hour_to_day(h):
        return h / 24


class EnergyConverter:
    TO_JOULE = {
        'J': 1.0,
        'kJ': 1000.0,
        'MJ': 1e6,
        'GJ': 1e9,
        'cal': 4.184,
        'kcal': 4184.0,
        'kWh': 3.6e6,
        'MWh': 3.6e9,
        'eV': 1.60218e-19,
        'keV': 1.60218e-16,
        'MeV': 1.60218e-13,
        'GeV': 1.60218e-10,
        'BTU': 1055.06,
        'erg': 1e-7,
        'ft-lb': 1.35582,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in EnergyConverter.TO_JOULE:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in EnergyConverter.TO_JOULE:
            raise ValueError(f"unknown unit : {to_unit}")

        joules = value * EnergyConverter.TO_JOULE[from_unit]
        return joules / EnergyConverter.TO_JOULE[to_unit]


    @staticmethod
    def joule_to_calorie(j):
        return j * 0.239006
    
    @staticmethod
    def calorie_to_joule(cal):
        return cal * 4.184
    
    @staticmethod
    def kilowatt_hour_to_joule(kwh):
        return kwh * 3.6e6
    
    @staticmethod
    def joule_to_kilowatt_hour(j):
        return j / 3.6e6
    
    @staticmethod
    def btu_to_joule(btu):
        return btu * 1055.06
    
    @staticmethod
    def joule_to_btu(j):
        return j / 1055.06


class PressureConverter:
    TO_PASCAL = {
        'Pa': 1.0,
        'kPa': 1000.0,
        'MPa': 1e6,
        'GPa': 1e9,
        'bar': 1e5,
        'mbar': 100.0,
        'atm': 101325.0,
        'Torr': 133.322,
        'mmHg': 133.322,
        'inHg': 3386.39,
        'psi': 6894.76,
        'ksi': 6.89476e6,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in PressureConverter.TO_PASCAL:
            raise ValueError(f"unknown unit : {from_unit}")
        if to_unit not in PressureConverter.TO_PASCAL:
            raise ValueError(f"unknown unit : {to_unit}")
        

        pascals = value * PressureConverter.TO_PASCAL[from_unit]
        return pascals / PressureConverter.TO_PASCAL[to_unit]
    

    @staticmethod
    def pascal_to_bar(pa):
        return pa * 1e-5
    
    @staticmethod
    def bar_to_pascal(bar):
        return bar * 1e5
    
    @staticmethod
    def atm_to_pascal(atm):
        return atm * 101325
    
    @staticmethod
    def pascal_to_atm(pa):
        return pa / 101325
    
    @staticmethod
    def psi_to_pascal(psi):
        return psi * 6894.76
    
    @staticmethod
    def pascal_to_psi(pa):
        return pa / 6894.76


class UnitConverter:
    def __init__(self):
        self.temperature = TemperatureConverter()
        self.length = LengthConverter()
        self.area = AreaConverter()
        self.volume = VolumeConverter()
        self.mass = MassConverter()
        self.speed = SpeedConverter()
        self.time = TimeConverter()
        self.energy = EnergyConverter()
        self.pressure = PressureConverter()