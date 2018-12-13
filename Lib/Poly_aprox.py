import numpy as np
import GaussSiedle_SOR as gs

def calcDominant(mat,b):
    mat = np.matrix(mat)
    newOrder = list(range(len(mat)))
    found = False
    for m in range(len(mat)):
        for n in range(m, len(mat)):
            if (abs(mat[n, m]) > abs(np.sum(mat[n:, m]) - mat[n, m])):
                newOrder.pop(n)
                newOrder.insert(m, n)
                found = True
                break
        if not found:
            return None
        mat = mat[newOrder,:]
        b=b[newOrder]
        newOrder = list(range(len(mat)))
        found=False
    return mat,b

def polynomial_approx(x, y):
    mat = []
    row = []
    for j in range(len(x)):
        for i in range(len(x)):
            z = lambda y : y ** (len(x) -i - 1)
            row.append(z(x[j]))
        mat.append(row)
        row = []
    mat = np.matrix(mat)
    y = [[10.5],[ 6.1], [3.5]]
    mat,y= calcDominant(mat,np.mat(y))
    return gs.SOR(mat,y)

def polynomial_calc(p, num, pow):
    sum = 0
    for i in range(pow + 1):
        sum = sum + p[i].item(0,0) * (num ** (pow - i))
    return sum
