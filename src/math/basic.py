"""
Basic math functions
"""

def add(numA: float, numB: float) -> float:
    """Add numA and numB"""
    return round(float(numA + numB), 2)

def sub(numA: float, numB: float) -> float:
    """Subtrate numA by numB"""
    return round(float(numA - numB), 2)

def mul(numA: float, numB: float) -> float:
    """Multiplicate numA by numB"""
    return round(float(numA * numB), 2)

def div(numA: float, numB: float) -> float:
    """Divide numA by numB"""
    if numB:
        return round(float(numA / numB), 2)
    raise ZeroDivisionError("Can't divide by zero!")

def mod(numA: float, numB: float) -> float:
    """Modulo numA by numB"""
    if numB:
        return round(float(numA % numB), 2)
    raise ZeroDivisionError("Can't divide by zero!")

def exp(num: float, exp: int) -> float:
    """Exponentiate num by exponent"""
    return round(float(num ** exp), 2)
