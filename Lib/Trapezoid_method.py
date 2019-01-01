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


# trapezoidal rule
def trapezoid(f,a,b,N):
    yi=[]
    h = (b-a)/N
    xi = find_intervals(a,b,N)
    for i in xi:
        yi.append(f(i))
    yi = np.asarray(yi)
    s = 0.0
    for i in range(1,N):
        if yi[i] != inf and yi[i] != -inf:
            s = s + yi[i]
            print("number iteration:",i)
            print("Approximation:",s)

    s = (h/2)*(yi[0] + yi[N]) + h*s
    return s



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
    print(trapezoid(fx, 1, 3, 100))
