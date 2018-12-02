from sympy import *
import cmath
import numpy as np
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

if __name__ == '__main__':
    x = Symbol('x')
    gx = exp(2*(x**2)-3*x)-4+cos(x**3+3)
    fx = func(gx)
    print(all_roots(fx, 0.0001, [-1,3], 100))