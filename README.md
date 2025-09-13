# dml
duck math library

A comprehensive Python library for mathematical computations, scientific calculations, unit conversions, and logical operations. This package provides a wide range of mathematical functions, constants, and utilities for various scientific and engineering applications.

## Features

### Mathematical Functions
- **Basic Operations**: Rounding, factorial, exponentiation, power functions
- **Number Theory**: Prime number detection, Fibonacci sequence operations
- **Logarithmic Functions**: Natural log, base-10 log, custom base logarithms
- **Trigonometric Functions**: Sine, cosine, tangent, and their inverses
- **Statistical Analysis**: Mean, median, mode, variance, standard deviation, percentiles

### Logical Gate Operations
- Basic gates: AND, OR, NOT, NAND, NOR, XOR, XNOR
- Bit shifting: SHL, SHR, arithmetic shift right
- Rotation: Rotate left, rotate right
- Multi-input operations: Multi-input AND, OR, XOR

### Unit Conversion System
Comprehensive conversion between units in various categories:
- **Temperature**: Celsius, Fahrenheit, Kelvin, Rankine
- **Length**: Meters, inches, feet, miles, light-years, parsecs
- **Area**: Square meters, acres, hectares, square feet
- **Volume**: Liters, gallons, cubic meters, cubic feet
- **Mass**: Kilograms, pounds, ounces, grams
- **Speed**: m/s, km/h, mph, knots, Mach
- **Time**: Seconds, minutes, hours, days, years
- **Energy**: Joules, calories, electronvolts, BTUs
- **Pressure**: Pascals, bars, atm, psi, mmHg

### Scientific Constants
Extensive collection of physical and mathematical constants:
- **Mathematical**: π, e, φ (golden ratio), Euler-Mascheroni constant
- **Physical**: Gravitational constant, Planck constant, speed of light
- **Astronomical**: Astronomical unit, light-year, parsec
- **Particle Physics**: Electron mass, proton mass, atomic mass unit
- **Engineering**: Standard gravity, standard atmosphere

## Installation

```bash
pip install ///
```

## Quick Start

```python
from dml import *

# Basic math operations
result = round(3.14159, 2)  # Returns 3.14
fact = factorial(5)         # Returns 120

# Number theory
is_fib = is_fib(8)          # Returns True (8 is a Fibonacci number)
is_prime = is_prime(17)     # Returns True (17 is prime)

# Unit conversion
temp = TemperatureConverter.convert(100, 'C', 'F')  # Returns 212°F
length = LengthConverter.convert(1, 'km', 'mile')   # Returns 0.621371 miles

# Statistical analysis
data = [1, 2, 3, 4, 5]
avg = mean(data)            # Returns 3.0
med = median(data)          # Returns 3

# Logical operations
result = AND(6, 3)          # Returns 2 (binary 110 & 011 = 010)
result = OR(6, 3)           # Returns 7 (binary 110 | 011 = 111)
```

## Detailed Usage

### Mathematical Functions

```python
# Exponential functions
e_value = exp(1)            # Returns e (approx. 2.71828)
power = int_power(2, 10)    # Returns 1024

# Fibonacci sequence
fib_num = nth_fib(10)       # Returns 55 (10th Fibonacci number)
fib_list = fib_between(10, 100)  # Returns [13, 21, 34, 55, 89]

# Prime numbers
next_prime = next_prime(10) # Returns 11
prime_factors = prime_factors(60)  # Returns [2, 2, 3, 5]

# Logarithms
ln_value = ln(10)           # Returns approx. 2.30258
log_value = log(100, 10)    # Returns 2

# Trigonometric functions
sin_value = sin(pi/2)       # Returns 1.0
arcsin_value = arcsin(1)    # Returns π/2
```

### Statistical Functions

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Central tendency
mean_val = mean(data)       # Returns 5.5
median_val = median(data)   # Returns 5.5
mode_val = mode([1, 2, 2, 3, 3, 3])  # Returns 3

# Dispersion
variance_val = variance(data)       # Returns 9.166...
std_dev = std_deviation(data)       # Returns approx. 3.027
data_range = data_r(data)           # Returns 9

# Specialized means
geom_mean = g_mean([2, 8])          # Returns 4.0
harm_mean = h_mean([2, 3])          # Returns 2.4
trimmed_mean = t_mean(data, 0.1)    # Returns 5.5 (trimming 10% from each end)

# Percentiles
percentile_val = percentile(data, 75)  # Returns 8.25 (75th percentile)
```

### Logical Operations

```python
# Basic gates
result = AND(6, 3)      # Returns 2 (binary: 110 & 011 = 010)
result = OR(6, 3)       # Returns 7 (binary: 110 | 011 = 111)
result = NOT(0, 8)      # Returns 255 (8-bit NOT of 0)

# Combined gates
result = NAND(6, 3, 8)  # Returns 253 (8-bit NAND of 6 and 3)
result = NOR(6, 3, 8)   # Returns 248 (8-bit NOR of 6 and 3)
result = XOR(6, 3)      # Returns 5 (binary: 110 ^ 011 = 101)
result = XNOR(6, 3, 8)  # Returns 250 (8-bit XNOR of 6 and 3)

# Bit shifting
result = SHL(5, 2)      # Returns 20 (binary: 101 << 2 = 10100)
result = SHR(20, 2)     # Returns 5 (binary: 10100 >> 2 = 101)

# Rotation
result = rotate_left(0b1100, 2, 4)   # Returns 0b0011 (4-bit rotation)
result = rotate_right(0b1100, 2, 4)  # Returns 0b0011 (4-bit rotation)

# Multi-input operations
result = multi_input_AND(3, 5, 7)    # Returns 1 (binary: 011 & 101 & 111 = 001)
result = multi_input_OR(1, 2, 4)     # Returns 7 (binary: 001 | 010 | 100 = 111)
result = multi_input_XOR(1, 3, 5)    # Returns 7 (binary: 001 ^ 011 ^ 101 = 111)
```

### Unit Conversion

```python
# Temperature conversion
c_to_f = TemperatureConverter.convert(100, 'C', 'F')  # 212°F
f_to_c = TemperatureConverter.convert(212, 'F', 'C')  # 100°C
k_to_c = TemperatureConverter.convert(273.15, 'K', 'C')  # 0°C

# Length conversion
km_to_mile = LengthConverter.convert(1, 'km', 'mile')  # 0.621371 miles
m_to_ft = LengthConverter.convert(1, 'm', 'ft')        # 3.28084 feet
ly_to_pc = LengthConverter.convert(1, 'ly', 'pc')      # 0.306601 parsecs

# Area conversion
acre_to_m2 = AreaConverter.convert(1, 'acre', 'm²')    # 4046.86 m²
ha_to_acre = AreaConverter.convert(1, 'ha', 'acre')    # 2.47105 acres

# Volume conversion
gal_to_l = VolumeConverter.convert(1, 'gal', 'l')      # 3.78541 liters
m3_to_ft3 = VolumeConverter.convert(1, 'm³', 'ft³')    # 35.3147 ft³

# Mass conversion
kg_to_lb = MassConverter.convert(1, 'kg', 'lb')        # 2.20462 pounds
oz_to_g = MassConverter.convert(1, 'oz', 'g')          # 28.3495 grams

# Speed conversion
kmh_to_mph = SpeedConverter.convert(100, 'km/h', 'mph')  # 62.1371 mph
mach_to_ms = SpeedConverter.convert(1, 'mach', 'm/s')    # 340.3 m/s

# Time conversion
day_to_hr = TimeConverter.convert(1, 'd', 'h')         # 24 hours
year_to_sec = TimeConverter.convert(1, 'yr', 's')      # 31,556,952 seconds

# Energy conversion
cal_to_j = EnergyConverter.convert(1, 'cal', 'J')      # 4.184 joules
ev_to_j = EnergyConverter.convert(1, 'eV', 'J')        # 1.60218e-19 joules

# Pressure conversion
atm_to_pa = PressureConverter.convert(1, 'atm', 'Pa')  # 101,325 pascals
psi_to_bar = PressureConverter.convert(1, 'psi', 'bar')  # 0.0689476 bar
```

### Constants Usage

```python
# Mathematical constants
print(MathematicalConstants.PI)      # 3.141592653589793
print(MathematicalConstants.E)       # 2.718281828459045
print(MathematicalConstants.PHI)     # 1.618033988749894 (golden ratio)

# Physical constants
print(LengthConstants.LIGHT_SPEED)   # 299792458 m/s
print(EnergyConstants.PLANCK_CONSTANT)  # 6.62607015e-34 J·s
print(GravitationalConstants.GRAVITATIONAL_CONSTANT)  # 6.67430e-11 m³/kg·s²

# Astronomical constants
print(LengthConstants.ASTRONOMICAL_UNIT)  # 1.495978707e11 m
print(LengthConstants.LIGHT_YEAR)         # 9.4607304725808e15 m
print(LengthConstants.PARSEC)             # 3.0856775814913673e16 m

# Engineering constants
print(TemperatureConstants.WATER_BOILING)  # 373.15 K (100°C)
print(PressureConstants.STANDARD_ATMOSPHERE)  # 101325 Pa
print(EngineeringConstants.STANDARD_GRAVITY)  # 9.80665 m/s²
```

## Help System

The package includes a comprehensive help system:

```python
# General help
help()

# List all functions
help(1)

# Detailed function descriptions
help(2)

# List all constants
help(3)

# Detailed constants descriptions
help(4)

# Package information
help(5)

# Help for specific functions
help('sin')
help('prime_factors')
help('TemperatureConverter')
```

## Requirements

- Python 3+
- No external dependencies

## License

MIT License - feel free to use this library in your projects.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you have any questions or issues, please open an issue on the GitHub repository.

## Version History

- 1.0.0: Initial release with comprehensive mathematical utilities, unit converters, and constants
