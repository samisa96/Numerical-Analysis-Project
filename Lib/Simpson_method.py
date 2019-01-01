import numpy as np
from math import *
from sympy import *
#import matplotlib.pyplot as plt

def f_sym(symbolic_fuction):
    return lambdify(x, symbolic_fuction)

def find_intervals(a, b, N):
    jump = (b - a)/N
    intervals = []
    j = a
    for i in range(N + 1):
        intervals.append(j)
        j = j + jump
    return np.array(intervals)


def simpson_method(f, a, b, n):
    if(n%2!=0):
        return 'n must be even'
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,n//2 + 1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    for i in range(1,n//2):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)


if __name__ == '__main__':
    x = Symbol('x')
    # fx = ln(x)
    # fx = x ** 2
    # fx = cos(x**3 - 1)
    # fx = sin(3 * x + 2)
    # fx = exp(x ** 2 + 4)
    # fx = sin(x**2 +5) - cos(x + 1)
    # fx = 1.00 / (sin(x + 1) + x ** 2)
    # fx = ln (x**2 - 2*x)
    fx = ln(x ** 2 - 2 * x) + cos(x ** 3 - 1) + exp(2 * (x ** 2) - 3 * x + 4)
    fx = f_sym(fx)
    print(simpson_method(fx, 1, 3, 100))
