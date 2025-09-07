import dml.basic_math as b
from dml.constants import MathematicalConstants as m

#--------------------------------------------------===| functions |===-----------------------------------------------


#---p1

def sin(angle: float, accuracy: int = 20) -> float:

    ang = angle
    ang = ang % (2 * m.PI)
    
    if abs(ang) < 1e-10 or abs(ang - m.PI) < 1e-10:
        return 0.0
    elif abs(ang - m.PI/2) < 1e-10:
        return 1.0
    elif abs(ang - 3*m.PI/2) < 1e-10:
        return -1.0
    
    result = 0.0
    for n in range(accuracy):
        term = ((-1)**n) * (ang**(2*n + 1)) / b.factorial(2*n + 1)
        result += term
    return result

def cos (angle:float , accuracy :int = 20)->float:
    ang = angle


    ang = ang % (2 * m.PI)


    if abs(ang) < 1e-10:  
        return 1.0
    elif abs(ang - m.PI) < 1e-10:  
        return -1.0
    elif abs(ang - m.PI/2) < 1e-10 or abs(ang - 3*m.PI/2) < 1e-10:  
        return 0.0


    result = 0.0
    for n in range(accuracy):
        term = ((-1) ** n) * (ang ** (2 * n)) / b.factorial(2 * n)
        result += term

    return result



def tan(angle: float, accuracy: int = 20) -> float:

    ang = angle
    ang = ang % (2 * m.PI)
    

    if abs(ang - m.PI/2) < 1e-10 or abs(ang - 3*m.PI/2) < 1e-10:
        raise ValueError("tan in this spot is no defined")
    
    return sin(ang, accuracy) / cos(ang, accuracy)

def cot(angle: float, accuracy: int = 20) -> float:
    
    ang = angle
    ang = ang % (2 * m.PI)
    

    if abs(ang) < 1e-10 or abs(ang - m.PI) < 1e-10:
        raise ValueError("cot in this spot is no defined")
    
    return cos(ang, accuracy) / sin(ang, accuracy)

#---p2

def arcsin(x: float, accuracy: int = 20) -> float:

    if x < -1 or x > 1:
        raise ValueError("The input must be between 1 and -1.")
    
    if abs(x) == 1:
        return m.PI/2 * x
    
    result = 0.0
    for n in range(accuracy):
        coeff = b.factorial(2*n) / (4**n * (b.factorial(n)**2) * (2*n + 1))
        result += coeff * (x**(2*n + 1))
    return result

def arccos(x: float, accuracy:int = 20) -> float:
    return m.PI/2 - arcsin(x, accuracy)

def arctan(x: float, accuracy: int = 20) -> float:
   
    if abs(x) > 1:
        return m.PI/2 - arctan(1/x) if x > 0 else -m.PI/2 - arctan(1/x)
    
    result = 0.0
    for n in range(accuracy):
        term = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        result += term
    return result