import dml.log as l
from dml.constants import MathematicalConstants as m

#------------------------------------------------------------------------l1-

def round(num: float, decimals: int = 0) -> float:
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be a number")
    
    if not isinstance(decimals, int):
        raise TypeError("Number of decimal places must be an integer")
    
    if decimals == 0:
        return int(num + (0.5 if num >= 0 else -0.5))
    
    multiplier = 10 ** decimals
    rounded_int = int(num * multiplier + (0.5 if num >= 0 else -0.5))
    return rounded_int / multiplier

def factorial(num:int) ->int:
    if num == 0:
        return 1
    result = 1
    for i in range(1 , num+1):
        result *= i
    return result

def radian(degree:float)-> float:
    d = (degree/180) * m.PI
    return d

def degree(radian:float)->float:
    r = (radian*180) / m.PI
    return r

#------------------------------------------------------------------------l2-

def exp(x, accuracy=50):
    result = 0
    for n in range(accuracy):
        term = (x ** n) / factorial(n)
        result += term
    return result

def int_power(x, power):
    b = 1
    for i in range(power):
        b *= x
    return b

def float_power(x, power:float):
    if x==0 and power > 0: return 0
    elif x==0 and power <= 0: return None
    elif x>0:
        return exp(power*l.ln(x))
    elif x<0:
        return None #The output is an imaginary number and is not supported here.

def pow(x:float, *power)->float:
    result = x
    for i in power:
        if (isinstance(i, (float))):
            result = float_power(result, i)
        elif(isinstance(i, (int))):
            result = int_power(result, i)

    return result