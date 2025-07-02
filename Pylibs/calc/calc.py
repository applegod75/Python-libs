import random
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

#this is a python library... At least i hope it will become that :)

def add(x ,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def Power(x, y):
    return x ** y

def squareRoot(x):
    return x ** 0.5

def exp(x, y):
    return x * 10 ** y

def factorial(x):
    prev_val = 1
    for i in range(x):
        prev_val *= i+1
    return prev_val

def randomNum(x, y):
    return random.randint(x, y)

def FractionToDecimal(x, y, z):
    return y / z + x

def DegToRad(x):
    return x * pi / 180

def RadToDeg(x):
    return x * 180 / pi

def CalculateTriangleArea(x, y):
    return x * y / 2
