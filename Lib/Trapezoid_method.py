import numpy as np
from sympy import *

def f(symbolic_function):
    return lambdify(x, symbolic_function)


def find_intervals(a, b, N):
    jump = (b - a)/N
    intervals = []
    j = a
    for i in range(N + 1):
        intervals.append(j)
        j = j + jump
    return np.array(intervals)


# trapezoidal rule
def trapezoid(f, a, b, N):
    h = (b-a)/N
    xi = find_intervals(a,b,N)
    fi = f(xi)
    s = 0.0
    for i in range(1,N):
        s = s + fi[i]
    s = (h/2)*(fi[0] + fi[N]) + h*s
    return s


if __name__ == "__main__":
    x = Symbol('x')
    #fx = cos(x ** 3 -1)
    #fx = ln(x)
    #fx = exp(x**2 + 4)
    #fx = sin(x ** 2 + 5) - cos(x + 1)
    #fx = 1.00/(sin(x+1)+x**2)
    fx = ln(x ** 2 - 2 * x) + cos(x**3 -1) + exp(2*(x**2) - 3*x + 4)
    fx = f(fx)
    print(trapezoid(fx, 1, 3, 100))