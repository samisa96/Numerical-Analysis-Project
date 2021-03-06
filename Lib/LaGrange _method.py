import numpy as np
from sympy import *

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def product(list):
    p = 1
    for i in list:
        p *= i
    return p
def printLagrange(X):
    x = Symbol('x')
    print("P = ",end="")
    for i in range(len(X)):
        print(X[i][1], "*", end = " ")
        for j in range(len(X) - 1):
            if i != j:
                print("(",x , "-",  X[j][0], ")/(",X[j][0], "-", X[j + 1][0], ")" , end = "")

        if(i!=len(X)-1):
            print(" + ", end = "")


def Lagrange(x,X):
    T = np.zeros((2,len(X)))
    list = []
    for i in range(len(X)):
        for j in range(len(X)):
            if i != j:
                list.append((x-X[j][0])/(X[i][0]-X[j][0]))
    p = []
    for i in chunkIt(list,len(X)):
        p.append(product(i))
    for i in range(len(X)):
        T[0][i] = p[i]
        T[1][i] = X[i][1]

    list2 = []
    for i in range(len(X)):
        list2.append(T[0][i]*T[1][i])
    return sum(list2)

print("General Lagranz polynomial approximation equation:")
print("P[n](x) = Sum(from i=0 to i=n) (L[i](x)*y[i])\n")
#x - The point that we place in the function
#X- POINTS
x, X = 0.35, [[2,-14],[1,-4],[0,0]]
#(2) x,X=1.5,[[5,2],[3,6],[-1,4]]
#(3) x,X=1.5,[[-7,2],[1,8.8],[-0.2,0.7]]
#(4) x,X=0.5,[[0,2],[1.5,6],[-5,4],[2,2]]
#(5) x,X=0.5,[[0,2],[1.5,6],[-5,4],[2,2],[5,5]]
#x,X=5,[[1,1],[2,2],[3,1],[4,1],[5,1]]
#x,X=0.35,[[0.2,0.19869],[0.3,0.295520],[0.4,0.389418],[0.5,0.479426]]
print("The approximated polynomial equation from the points",X," is:")
printLagrange(X)
print()
print("\nThe result of the approximated equation at value x=",x," is:")
print("P(",x,")= ",Lagrange(x,X))
#(1) - result - -0.71749
#(2) - result - 6.8125
#(3) - result - 12.9125
#(4) - result - 5.3780
#(5) - result - 6.37225