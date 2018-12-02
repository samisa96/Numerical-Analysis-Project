from math import *
import cmath
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')

def find_roots(rangex):
    intervals = []
    j = rangex[0]
    for _ in range((abs(rangex[1])+abs(rangex[0])) * 2):
        intervals.append([j, j + 0.5])
        j = j + 0.5
    return intervals

def checkVariable(root, roots, eps):
    for i in roots:
        if abs(i - root) < eps:
            return  False
    return True

def checkRoot(f,root, eps):
    return abs(f(root)) < eps

def secant(rangex, fx, x0, x1, eps, itration,printList):
    i=0
    while abs(x1 - x0) > eps or itration == 0:
        if abs(fx(x1) - fx(x0)) < eps:
            return None
        x = x1 - fx(x1) * ((x1 - x0)/(fx(x1) - fx(x0)))
        printList.append((x,i))
        i += 1
        x0 = x1
        x1 = x
        itration -= 1
    return x

def Print_roots(printList):
    for i in printList:
        print("number iteration:", i[1])
        print("Approximation:", i[0])

def all_roots(fx, eps, rangex, itration):
    roots = []
    intervals = find_roots(rangex)
    for i in intervals:
        printList=[]
        x0 = (i[0] + i[1]) / 3
        x1 = (i[0] + i[1]) / 2
        root = secant(rangex, fx, x0, x1, eps, itration,printList)

        if root != None:
            if(len(roots)==0):
                if root >= rangex[0] and root <= rangex[1] and checkRoot(fx, root, eps):
                    roots.append(root)
                    Print_roots(printList)
            else:
                if root == None:
                    continue
                if (not checkVariable(root, roots, 0.1)):
                    continue
                if fx(root) == None:
                    continue
                elif root <= rangex[1] and root >= rangex[0] and checkRoot(fx, root, eps):
                    roots.append(root)
                    Print_roots(printList)
    if len(roots) == 0:
        return None
    return roots

def plot_it(start, end, function, methodName):
    '''
    :param start: Start of interval
    :type start: float
    :param end: End of interval
    :type end: float
    :param function: function
    :type function: lambda
    :param methodName: Method name - for the Title
    :type methodName: string
    '''
    # Data for plotting
    t = np.arange(start, end, 0.01)
    s = function(t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='X', ylabel='Y',
        title = methodName)
    ax.grid()

    fig.savefig("test.png")
    plt.show()

if __name__ == '__main__':
    x = Symbol('x')
    gx = exp(2*(x**2)-3*x)-4+cos(x**3+3)
    fx = func(gx)
    rang = [-1,3]
    print(all_roots(fx, 0.0001, rang, 100))

    #plot the function:
    plot_it(rang[0],rang.pop(),fx, "Secant Method")