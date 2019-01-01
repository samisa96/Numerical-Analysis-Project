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

# romberg method
def romberg(f,a,b,eps,nmax):
# f     ... function to be integrated
# [a,b] ... integration interval
# eps   ... desired accuracy
# nmax  ... maximal order of Romberg method
    Q = np.zeros((nmax,nmax),float)
    converged = 0
    k=0
    for i in range(0,nmax):
        N = 2**i
        Q[i,0] = trapezoid(f,a,b,N)
        for k in range(0,i):
            n = k + 2
            Q[i,k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Q[i,k] - Q[i-1,k])
            print("number iteration:",k)
            print("Approximation:",Q[i,k])
        if (i > 0):
            if (abs(Q[i,k+1] - Q[i,k]) < eps):
               converged = 1
               break
    if nmax == 1:
        return Q[i,k],k
    return Q[i,k + 1],k


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
    print(romberg(fx, 1, 3,0.001, 100))
