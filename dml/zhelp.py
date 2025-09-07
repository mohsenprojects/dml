def help(i=0):
    """
    Display help information for the math utilities package.
    
    Args:
        i (int or str): Help mode or function name to get details about
            - 0: Basic help overview
            - 1: Function names list
            - 2: Detailed function descriptions
            - 3: Constants names list
            - 4: Constants descriptions
            - 5: Package information
            - function name: Detailed info about specific function
    """
    # If i is a string (function name), show specific function help
    if isinstance(i, str):
        function_help(i.lower())
        return
    
    # Numeric help modes
    if i == 0:
        print("Math Utilities Package Help\n" \
              "==========================\n" \
              "help(1): List of all function names\n" \
              "help(2): Detailed function descriptions with examples\n" \
              "help(3): List of all constants\n" \
              "help(4): Detailed constants descriptions\n" \
              "help(5): Package information and developer details\n" \
              "help('function_name'): Detailed information about a specific function")
    
    elif i == 1:
        print("Available Functions:\n" \
              "===================\n" \
              "Basic Math Functions:\n" \
              "  round(num, decimals=0), factorial(num), radian(degree), degree(radian)\n" \
              "  exp(x, accuracy), int_power(x, power), float_power(x, power), pow(x, *powers)\n\n" \
              "Fibonacci Functions:\n" \
              "  is_fib(num), nth_fib(n), fib_between(start, lim), nth_fib_list(start, end)\n\n" \
              "Prime Number Functions:\n" \
              "  is_prime(num), next_prime(num), prev_prime(num), prime_factors(num)\n" \
              "  nth_prime(num), primes_between(start, lim), nth_prime_list(start, lim)\n" \
              "  number_of_primes_between_range(start, lim)\n\n" \
              "Logarithm Functions:\n" \
              "  ln(x, terms=100), log(x, base=10, terms=100), log2(x), log10(x)\n\n" \
              "Trigonometric Functions:\n" \
              "  sin(x, accuracy=20), cos(x, accuracy=20), tan(x, accuracy=20), cot(x, accuracy=20)\n" \
              "  arcsin(x, accuracy), arccos(x, accuracy), arctan(x, accuracy)\n\n" \
              "Statistical Functions:\n" \
              "  mean(nums), median(nums), mode(nums), g_mean(nums), h_mean(nums)\n" \
              "  t_mean(nums, trim_percent), variance(nums), pvariance(nums)\n" \
              "  std_deviation(nums), std_pdeviation(nums), data_r(nums), percentile(nums, p)\n\n" \
              "Logical Gates:\n" \
              "  AND(a, b), OR(a, b), NOT(a, bit_length=32), NAND(a, b, bit_length=32)\n" \
              "  NOR(a, b, bit_length=32), XOR(a, b), XNOR(a, b, bit_length=32)\n" \
              "  SHL(a, n_bits=1), SHR(a, n_bits=1), arithmetic_shift_right(a, n_bits=1, bit_length=32)\n" \
              "  rotate_left(a, n_bits, bit_length=32), rotate_right(a, n_bits, bit_length=32)\n" \
              "  multi_input_AND(*numbers, bit_length=32), multi_input_OR(*numbers, bit_length=32)\n" \
              "  multi_input_XOR(*numbers, bit_length=32)\n\n" \
              "Unit Converters:\n" \
              "  TemperatureConverter, LengthConverter, AreaConverter, VolumeConverter\n" \
              "  MassConverter, SpeedConverter, TimeConverter, EnergyConverter, PressureConverter\n" \
              "  UnitConverter (comprehensive converter)")
    
    elif i == 2:
        print("Detailed Function Descriptions:\n" \
              "=============================\n" \
              "Basic Math Functions:\n" \
              "  round(num, decimals=0): Rounds a number to specified decimal places\n" \
              "  factorial(num): Calculates the factorial of a number\n" \
              "  radian(degree): Converts degrees to radians\n" \
              "  degree(radian): Converts radians to degrees\n" \
              "  exp(x, accuracy): Calculates e^x with specified accuracy\n" \
              "  int_power(x, power): Calculates integer powers efficiently\n" \
              "  float_power(x, power): Calculates floating-point powers\n" \
              "  pow(x, *powers): Calculates multiple powers in sequence\n\n" \
              "Fibonacci Functions:\n" \
              "  is_fib(num): Checks if a number is in the Fibonacci sequence\n" \
              "  nth_fib(n): Returns the nth Fibonacci number\n" \
              "  fib_between(start, lim): Returns Fibonacci numbers between a range\n" \
              "  nth_fib_list(start, end): Returns a list of Fibonacci numbers from start to end indices\n\n" \
              "Prime Number Functions:\n" \
              "  is_prime(num): Checks if a number is prime\n" \
              "  next_prime(num): Finds the next prime after a number\n" \
              "  prev_prime(num): Finds the previous prime before a number\n" \
              "  prime_factors(num): Returns prime factors of a number\n" \
              "  nth_prime(num): Returns the nth prime number\n" \
              "  primes_between(start, lim): Finds primes between a range\n" \
              "  nth_prime_list(start, lim): Returns a list of primes from start to end indices\n" \
              "  number_of_primes_between_range(start, lim): Estimates prime count in a range\n\n" \
              "Logarithm Functions:\n" \
              "  ln(x, terms=100): Calculates natural logarithm with specified precision\n" \
              "  log(x, base=10, terms=100): Calculates logarithm with any base\n" \
              "  log2(x): Calculates base-2 logarithm\n" \
              "  log10(x): Calculates base-10 logarithm\n\n" \
              "Trigonometric Functions:\n" \
              "  sin(x, accuracy=20): Calculates sine with specified accuracy\n" \
              "  cos(x, accuracy=20): Calculates cosine with specified accuracy\n" \
              "  tan(x, accuracy=20): Calculates tangent with specified accuracy\n" \
              "  cot(x, accuracy=20): Calculates cotangent with specified accuracy\n" \
              "  arcsin(x, accuracy): Calculates inverse sine (arcsine)\n" \
              "  arccos(x, accuracy): Calculates inverse cosine (arccosine)\n" \
              "  arctan(x, accuracy): Calculates inverse tangent (arctangent)\n\n" \
              "Statistical Functions:\n" \
              "  mean(nums): Calculates arithmetic mean of a list\n" \
              "  median(nums): Calculates median of a list\n" \
              "  mode(nums): Finds mode(s) of a list\n" \
              "  g_mean(nums): Calculates geometric mean\n" \
              "  h_mean(nums): Calculates harmonic mean\n" \
              "  t_mean(nums, trim_percent): Calculates trimmed mean\n" \
              "  variance(nums): Calculates sample variance\n" \
              "  pvariance(nums): Calculates population variance\n" \
              "  std_deviation(nums): Calculates sample standard deviation\n" \
              "  std_pdeviation(nums): Calculates population standard deviation\n" \
              "  data_r(nums): Calculates data range\n" \
              "  percentile(nums, p): Calculates percentile value\n\n" \
              "For detailed information about a specific function, use help('function_name')")
    
    elif i == 3:
        print("Available Constants:\n" \
              "===================\n" \
              "MathematicalConstants: PI, E, PHI, EULER_MASCHERONI, IMAGINARY_UNIT, APERY, CATALAN, etc.\n" \
              "LengthConstants: METER, KILOMETER, INCH, FOOT, YARD, MILE, LIGHT_YEAR, PARSEC, etc.\n" \
              "AreaConstants: SQUARE_METER, SQUARE_KILOMETER, HECTARE, ACRE, SQUARE_MILE, etc.\n" \
              "VolumeConstants: CUBIC_METER, LITER, GALLON_US, GALLON_UK, CUBIC_INCH, etc.\n" \
              "MassConstants: KILOGRAM, GRAM, POUND, OUNCE, ELECTRON_MASS, PROTON_MASS, etc.\n" \
              "TemperatureConstants: KELVIN, CELSIUS_OFFSET, ABSOLUTE_ZERO points, etc.\n" \
              "TimeConstants: SECOND, MINUTE, HOUR, DAY, WEEK, YEAR, PLANCK_TIME, etc.\n" \
              "SpeedConstants: METER_PER_SECOND, KILOMETER_PER_HOUR, MILE_PER_HOUR, LIGHT_SPEED, etc.\n" \
              "And many more constants across various scientific domains...\n\n" \
              "Use help(4) for detailed descriptions or help('ConstantClass') for specific constant classes.")
    
    elif i == 4:
        print("Detailed Constants Descriptions:\n" \
              "==============================\n" \
              "MathematicalConstants: Fundamental mathematical constants like π, e, φ (golden ratio)\n" \
              "LengthConstants: Conversion factors for various length units from metric to astronomical\n" \
              "AreaConstants: Conversion factors for area measurements across different systems\n" \
              "VolumeConstants: Conversion factors for volume measurements including fluid ounces\n" \
              "MassConstants: Mass conversion factors and fundamental particle masses\n" \
              "TemperatureConstants: Temperature scales and significant temperature points\n" \
              "TimeConstants: Time units from nanoseconds to millennia and scientific time constants\n" \
              "SpeedConstants: Speed units from m/s to light speed and Mach number\n" \
              "PressureConstants: Pressure units from Pascals to PSI and atmospheric pressure\n" \
              "EnergyConstants: Energy units from Joules to electronvolts and BTUs\n" \
              "And many more specialized constants for various scientific calculations...\n\n" \
              "Use help('ConstantClass') for detailed information about specific constant classes.")
    
    elif i == 5:
        print("Package Information:\n" \
              "===================\n" \
              "Math Utilities Package\n" \
              "Version: 1.0.0\n" \
              "Comprehensive mathematical and scientific computing library\n\n" \
              "Features:\n" \
              "- Advanced mathematical functions and operations\n" \
              "- Number theory utilities (primes, Fibonacci sequences)\n" \
              "- Statistical analysis and probability functions\n" \
              "- Logical gate operations and bit manipulation\n" \
              "- Extensive unit conversion system\n" \
              "- Comprehensive scientific constants library\n\n" \
              "Developer: Mohsen\n" \
              "Contact: mohsent680t@gmail.com\n" \
              "License: MIT Open Source")
    
    else:
        print(f"Invalid help option: {i}\nUse help() or help(0) for available options.")


def function_help(func_name):
    """Display detailed help for a specific function"""
    help_texts = {
        # Basic Math Functions
        "round": "Round a number to specified decimal places\nUsage: round(number, decimals=0)\nExample: round(3.14159, 2) returns 3.14",
        "factorial": "Calculate the factorial of a number\nUsage: factorial(n)\nExample: factorial(5) returns 120",
        "radian": "Convert degrees to radians\nUsage: radian(degrees)\nExample: radian(180) returns π (approx. 3.14159)",
        "degree": "Convert radians to degrees\nUsage: degree(radians)\nExample: degree(π) returns 180",
        "exp": "Calculate exponential function e^x\nUsage: exp(x, accuracy=100)\nExample: exp(1) returns e (approx. 2.71828)",
        "int_power": "Calculate integer powers efficiently\nUsage: int_power(x, power)\nExample: int_power(2, 10) returns 1024",
        "float_power": "Calculate floating-point powers\nUsage: float_power(x, power)\nExample: float_power(4, 0.5) returns 2.0",
        "pow": "Calculate multiple powers in sequence\nUsage: pow(x, *powers)\nExample: pow(2, 3, 4) calculates 2^3^4",
        
        # Fibonacci Functions
        "is_fib": "Check if a number is in the Fibonacci sequence\nUsage: is_fib(num)\nExample: is_fib(8) returns True",
        "nth_fib": "Get the nth Fibonacci number\nUsage: nth_fib(n)\nExample: nth_fib(10) returns 34",
        "fib_between": "Get Fibonacci numbers between a range\nUsage: fib_between(start, end)\nExample: fib_between(10, 100) returns [13, 21, 34, 55, 89]",
        "nth_fib_list": "Get a list of Fibonacci numbers from start to end indices\nUsage: nth_fib_list(start, end)\nExample: nth_fib_list(5, 10) returns [5, 8, 13, 21, 34, 55]",
        
        # Prime Number Functions
        "is_prime": "Check if a number is prime\nUsage: is_prime(num)\nExample: is_prime(17) returns True",
        "next_prime": "Find the next prime after a number\nUsage: next_prime(num)\nExample: next_prime(10) returns 11",
        "prev_prime": "Find the previous prime before a number\nUsage: prev_prime(num)\nExample: prev_prime(20) returns 19",
        "prime_factors": "Get prime factors of a number\nUsage: prime_factors(num)\nExample: prime_factors(60) returns [2, 2, 3, 5]",
        "nth_prime": "Get the nth prime number\nUsage: nth_prime(n)\nExample: nth_prime(5) returns 11",
        "primes_between": "Find primes between a range\nUsage: primes_between(start, end)\nExample: primes_between(10, 30) returns [11, 13, 17, 19, 23, 29]",
        "nth_prime_list": "Get a list of primes from start to end indices\nUsage: nth_prime_list(start, end)\nExample: nth_prime_list(5, 10) returns [11, 13, 17, 19, 23, 29]",
        "number_of_primes_between_range": "Estimate prime count in a range\nUsage: number_of_primes_between_range(start, end)\nExample: number_of_primes_between_range(1, 100) returns 25",
        
        # Logarithm Functions
        "ln": "Calculate natural logarithm\nUsage: ln(x, terms=100)\nExample: ln(10) returns approx. 2.30258",
        "log": "Calculate logarithm with any base\nUsage: log(x, base=10, terms=100)\nExample: log(100, 10) returns 2",
        "log2": "Calculate base-2 logarithm\nUsage: log2(x)\nExample: log2(8) returns 3",
        "log10": "Calculate base-10 logarithm\nUsage: log10(x)\nExample: log10(1000) returns 3",
        
        # Trigonometric Functions
        "sin": "Calculate sine of an angle in radians\nUsage: sin(x, accuracy=20)\nExample: sin(π/2) returns 1.0",
        "cos": "Calculate cosine of an angle in radians\nUsage: cos(x, accuracy=20)\nExample: cos(0) returns 1.0",
        "tan": "Calculate tangent of an angle in radians\nUsage: tan(x, accuracy=20)\nExample: tan(π/4) returns 1.0",
        "cot": "Calculate cotangent of an angle in radians\nUsage: cot(x, accuracy=20)\nExample: cot(π/4) returns 1.0",
        "arcsin": "Calculate inverse sine (arcsine)\nUsage: arcsin(x, accuracy=20)\nExample: arcsin(1) returns π/2",
        "arccos": "Calculate inverse cosine (arccosine)\nUsage: arccos(x, accuracy=20)\nExample: arccos(0) returns π/2",
        "arctan": "Calculate inverse tangent (arctangent)\nUsage: arctan(x, accuracy=20)\nExample: arctan(1) returns π/4",
        
        # Statistical Functions
        "mean": "Calculate arithmetic mean\nUsage: mean(numbers)\nExample: mean([1, 2, 3, 4]) returns 2.5",
        "median": "Calculate median\nUsage: median(numbers)\nExample: median([1, 2, 3, 4, 5]) returns 3",
        "mode": "Find mode(s)\nUsage: mode(numbers)\nExample: mode([1, 2, 2, 3, 3, 3]) returns 3",
        "g_mean": "Calculate geometric mean\nUsage: g_mean(numbers)\nExample: g_mean([2, 8]) returns 4.0",
        "h_mean": "Calculate harmonic mean\nUsage: h_mean(numbers)\nExample: h_mean([2, 3]) returns 2.4",
        "t_mean": "Calculate trimmed mean\nUsage: t_mean(numbers, trim_percent)\nExample: t_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0.1) returns 5.5",
        "variance": "Calculate sample variance\nUsage: variance(numbers)\nExample: variance([1, 2, 3, 4, 5]) returns 2.5",
        "pvariance": "Calculate population variance\nUsage: pvariance(numbers)\nExample: pvariance([1, 2, 3, 4, 5]) returns 2.0",
        "std_deviation": "Calculate sample standard deviation\nUsage: std_deviation(numbers)\nExample: std_deviation([1, 2, 3, 4, 5]) returns approx. 1.581",
        "std_pdeviation": "Calculate population standard deviation\nUsage: std_pdeviation(numbers)\nExample: std_pdeviation([1, 2, 3, 4, 5]) returns approx. 1.414",
        "data_r": "Calculate data range\nUsage: data_r(numbers)\nExample: data_r([1, 5, 3, 9, 2]) returns 8",
        "percentile": "Calculate percentile value\nUsage: percentile(numbers, p)\nExample: percentile([1, 2, 3, 4, 5], 50) returns 3",
        
        # Logical Gates
        "and": "Bitwise AND operation\nUsage: AND(a, b)\nReturns: a & b\nExample: AND(6, 3) returns 2 (binary 110 & 011 = 010)",
        "or": "Bitwise OR operation\nUsage: OR(a, b)\nReturns: a | b\nExample: OR(6, 3) returns 7 (binary 110 | 011 = 111)",
        "not": "Bitwise NOT operation with specified bit length\nUsage: NOT(a, bit_length=32)\nReturns: ~a masked to bit_length\nExample: NOT(0, 8) returns 255",
        "nand": "Bitwise NAND operation\nUsage: NAND(a, b, bit_length=32)\nReturns: NOT(AND(a, b), bit_length)\nExample: NAND(6, 3, 8) returns 253",
        "nor": "Bitwise NOR operation\nUsage: NOR(a, b, bit_length=32)\nReturns: NOT(OR(a, b), bit_length)\nExample: NOR(6, 3, 8) returns 248",
        "xor": "Bitwise XOR operation\nUsage: XOR(a, b)\nReturns: a ^ b\nExample: XOR(6, 3) returns 5 (binary 110 ^ 011 = 101)",
        "xnor": "Bitwise XNOR operation\nUsage: XNOR(a, b, bit_length=32)\nReturns: NOT(XOR(a, b), bit_length)\nExample: XNOR(6, 3, 8) returns 250",
        "shl": "Shift left operation\nUsage: SHL(a, n_bits=1)\nReturns: a << n_bits\nExample: SHL(5, 2) returns 20",
        "shr": "Shift right operation\nUsage: SHR(a, n_bits=1)\nReturns: a >> n_bits\nExample: SHR(20, 2) returns 5",
        "arithmetic_shift_right": "Arithmetic shift right (preserves sign)\nUsage: arithmetic_shift_right(a, n_bits=1, bit_length=32)\nExample: arithmetic_shift_right(-8, 1, 8) returns -4",
        "rotate_left": "Rotate left operation\nUsage: rotate_left(a, n_bits, bit_length=32)\nExample: rotate_left(0b1100, 2, 4) returns 0b0011",
        "rotate_right": "Rotate right operation\nUsage: rotate_right(a, n_bits, bit_length=32)\nExample: rotate_right(0b1100, 2, 4) returns 0b0011",
        "multi_input_and": "Multi-input AND operation\nUsage: multi_input_AND(*numbers, bit_length=32)\nExample: multi_input_AND(3, 5, 7) returns 1",
        "multi_input_or": "Multi-input OR operation\nUsage: multi_input_OR(*numbers, bit_length=32)\nExample: multi_input_OR(1, 2, 4) returns 7",
        "multi_input_xor": "Multi-input XOR operation\nUsage: multi_input_XOR(*numbers, bit_length=32)\nExample: multi_input_XOR(1, 3, 5) returns 7",
        
        # Unit Converters
        "temperatureconverter": "Temperature conversion between various scales\nSupports: Celsius, Fahrenheit, Kelvin, Rankine\nUsage: TemperatureConverter.convert(value, from_unit, to_unit)\nExample: TemperatureConverter.convert(100, 'C', 'F') returns 212",
        "lengthconverter": "Length conversion between various units\nSupports: meters, inches, feet, miles, light-years, etc.\nUsage: LengthConverter.convert(value, from_unit, to_unit)\nExample: LengthConverter.convert(1, 'km', 'mile') returns 0.621371",
        "areaconverter": "Area conversion between various units\nSupports: square meters, acres, hectares, square feet, etc.\nUsage: AreaConverter.convert(value, from_unit, to_unit)\nExample: AreaConverter.convert(1, 'acre', 'm²') returns 4046.86",
        "volumeconverter": "Volume conversion between various units\nSupports: liters, gallons, cubic meters, cubic feet, etc.\nUsage: VolumeConverter.convert(value, from_unit, to_unit)\nExample: VolumeConverter.convert(1, 'gallon', 'liter') returns 3.78541",
        "massconverter": "Mass conversion between various units\nSupports: kilograms, pounds, ounces, grams, etc.\nUsage: MassConverter.convert(value, from_unit, to_unit)\nExample: MassConverter.convert(1, 'kg', 'pound') returns 2.20462",
        "speedconverter": "Speed conversion between various units\nSupports: m/s, km/h, mph, knots, etc.\nUsage: SpeedConverter.convert(value, from_unit, to_unit)\nExample: SpeedConverter.convert(100, 'km/h', 'mph') returns 62.1371",
        "timeconverter": "Time conversion between various units\nSupports: seconds, minutes, hours, days, years, etc.\nUsage: TimeConverter.convert(value, from_unit, to_unit)\nExample: TimeConverter.convert(1, 'day', 'hour') returns 24",
        "energyconverter": "Energy conversion between various units\nSupports: joules, calories, electronvolts, BTUs, etc.\nUsage: EnergyConverter.convert(value, from_unit, to_unit)\nExample: EnergyConverter.convert(1, 'calorie', 'joule') returns 4.184",
        "pressureconverter": "Pressure conversion between various units\nSupports: pascals, bars, atm, psi, mmHg, etc.\nUsage: PressureConverter.convert(value, from_unit, to_unit)\nExample: PressureConverter.convert(1, 'atm', 'pascal') returns 101325",
        "unitconverter": "Comprehensive unit converter with access to all conversion classes\nUsage: UnitConverter().length.convert(value, from_unit, to_unit)",
        
        # Constants
        "mathematicalconstants": "Mathematical constants class\nContains: PI, E, PHI, EULER_MASCHERONI, IMAGINARY_UNIT, APERY, CATALAN, etc.\nUsage: MathematicalConstants.PI",
        "lengthconstants": "Length constants class\nContains: METER, KILOMETER, INCH, FOOT, YARD, MILE, LIGHT_YEAR, PARSEC, etc.\nUsage: LengthConstants.METER",
        "areaconstants": "Area constants class\nContains: SQUARE_METER, SQUARE_KILOMETER, HECTARE, ACRE, SQUARE_MILE, etc.\nUsage: AreaConstants.SQUARE_METER",
        "volumeconstants": "Volume constants class\nContains: CUBIC_METER, LITER, GALLON_US, GALLON_UK, CUBIC_INCH, etc.\nUsage: VolumeConstants.LITER",
        "massconstants": "Mass constants class\nContains: KILOGRAM, GRAM, POUND, OUNCE, ELECTRON_MASS, PROTON_MASS, etc.\nUsage: MassConstants.KILOGRAM",
        "temperatureconstants": "Temperature constants class\nContains: KELVIN, CELSIUS_OFFSET, ABSOLUTE_ZERO points, etc.\nUsage: TemperatureConstants.KELVIN",
        "timeconstants": "Time constants class\nContains: SECOND, MINUTE, HOUR, DAY, WEEK, YEAR, PLANCK_TIME, etc.\nUsage: TimeConstants.SECOND",
        "speedconstants": "Speed constants class\nContains: METER_PER_SECOND, KILOMETER_PER_HOUR, MILE_PER_HOUR, LIGHT_SPEED, etc.\nUsage: SpeedConstants.LIGHT_SPEED",
        "pressureconstants": "Pressure constants class\nContains: PASCAL, KILOPASCAL, MEGAPASCAL, BAR, ATM, PSI, etc.\nUsage: PressureConstants.ATM",
        "energyconstants": "Energy constants class\nContains: JOULE, KILOJOULE, MEGAJOULE, CALORIE, ELECTRONVOLT, BTU, etc.\nUsage: EnergyConstants.JOULE",
    }
    
    if func_name in help_texts:
        print(f"Help for {func_name}:\n{help_texts[func_name]}")
    else:
        print(f"No detailed help available for '{func_name}'. Use help(1) to see all available functions.")