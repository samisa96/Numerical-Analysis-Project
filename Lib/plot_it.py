import numpy as np
import matplotlib.pyplot as plt
from math import *
import sympy as sym

def plot_it(start, end, function, methodName):#A function used for drawing graphs
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

if "__main__" == __name__:

    func = lambda x:np.log(x**2)-np.cos(x)+np.sin((x**2)-4)
    #func = lambda x: np.log(x**2-2*x)-np.cos(x+3)
    plot_it(-10,10,func, "METHOD NAME")
