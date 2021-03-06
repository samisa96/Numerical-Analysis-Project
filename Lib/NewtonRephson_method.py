import cmath
from math import *
from sympy import *
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def func(symbolic_fuction):
    return lambdify(x, symbolic_fuction, 'numpy')

def derivative(symbolic_fuction):
    g_tagx = diff(symbolic_fuction)
    return lambdify(x, g_tagx, 'numpy')

def slice(rangex):
    intervals = []
    j = rangex[0]
    while j <= rangex[1]:
        intervals.append([j, j + 0.05])
        j = j + 0.05

    return intervals

def NR(f, f_tag, x,eps, itration,printList):
    i=0
    while abs(f(x)) > eps or itration == 0:
        if f_tag(x) == 0:
            return None
        print("     Itertation number: ", i)
        print("     Old guess is: ", x)
        x = x - f(x) / f_tag(x)
        print("     Next guess is: ", x,'\n')
        printList.append((x, i))
        i += 1
        itration -= 1
    return x

def checkVariable(root, roots, eps):
    for i in roots:
        if abs(i - root) < eps:
            return  False
    return True

def checkRoot(f,root, eps):
    return abs(f(root)) < eps

def Print_roots(printList):
    for i in printList:
        print("Iteration number: ", i[1])
        print("Approximation root is: ", i[0],'\n')

def all_roots(f, f_tag, eps, rangex, itration):
    j = 1
    print("***********************************************************")
    print("** Newton Raphson Formula is: X(r+1) = Xr - F(x) / F'(x) **")
    print("***********************************************************",'\n')
    roots = []
    intervals = slice(rangex)
    for i in intervals:
        printList=[]
        x = (i[0] + i[1]) / 2
        print("Interval number", j, "is: ", i, "\n     the first guess is: ", x,'\n')
        j += 1
        root = NR(f, f_tag, x, eps, itration, printList)
        if root != None:
            if (len(roots)==0)and  root <= rangex[1] and root >= rangex[0] and checkRoot(f, root, eps):
                print("*****************************************")
                print("ROOT IS: [", root, ']')
                print("*****************************************\n")


                roots.append(root)
                #Print_roots(printList)
            else:
                if root == None:
                    continue
                if (not checkVariable(root, roots, 0.1)):
                    continue
                if f(root) == None:
                    continue
                elif root <= rangex[1] and root >= rangex[0] and checkRoot(f, root, eps):
                    print("*****************************************")
                    print("ROOT IS: [", root, ']')
                    print("*****************************************\n")
                    roots.append(root)
                    #Print_roots(printList)

    if len(roots) == 0:
        return None
    roots.sort()
    print("The root list is: ", roots)
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
    t = np.arange(start, end, 0.00001)
    s = function(t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='X', ylabel='Y',
        title = methodName)
    ax.grid()

    fig.savefig("test.png")
    plt.show()


if '__main__' == __name__:

    x = Symbol('x')
###########################################################
############# Write down the function: ####################
###########################################################
    fx = cos(x**2 + 4)
    #sin(x**2 + 4)
    #sin(x) + (ln(x)* cos(x))
    #x * exp(-x) - 0.25
###########################################################
    tmp = func(fx)
    xtag = derivative(fx)
    fx = tmp
###########################################################
############# Write down the parameters: ##################
###########################################################
    range = [-3, 3]
    epsilon = 0.001
    iteration = 100
###########################################################
    roots = all_roots(tmp, xtag, epsilon, range, iteration)
    plot_it(-10, 10, tmp, 'Newton Rephson')