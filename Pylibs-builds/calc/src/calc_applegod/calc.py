import random
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

#this is a python library... At least i hope it will become that :)

def add(x ,y):
    """Adds 'x' to 'y' and returns the answer"""

    return x + y

def subtract(x, y):
    """subtracts 'x' from 'y' and returns the answer"""
    return x - y

def multiply(x, y):
    """multiplies 'x' with 'y' then returns the answer"""
    return x * y

def divide(x, y):
    """divides 'x' by 'y' then returns the answer"""
    return x / y

def Power(x, y):
    """sets 'x' to the power of 'y' then returns the answer"""
    return x ** y

def squareRoot(x):
    """returns the square root of 'x'"""
    return x ** 0.5

def exp(x, y):
    """returns exxponent 'y' added to 'x'"""
    return x * 10 ** y

def factorial(x):
    """returns the factorial of 'x'"""
    prev_val = 1
    for i in range(x):
        prev_val *= i+1
    return prev_val

def randomNum(x, y):
    """returns a raandom number between 'x' and 'y'"""
    return random.randint(x, y)

def FractionToDecimal(x, y, z) -> float:
    """ sets a fraction to a decimal.
    
        if x=1 y=2 z=3:
            fraction = 1 2/3
        X is None by default
    """
    return y / z + x

def DegToRad(x):
    """ turns degrees to a radians"""

    return x * pi / 180

def RadToDeg(x):
    """ turns radians to degrees"""
    return x * 180 / pi

def CalculateTriangleArea(x, y):
    """calculate triangle area with length and width"""
    return x * y / 2
