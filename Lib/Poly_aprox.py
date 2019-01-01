import numpy as np
import SOR as gs


def StrongcalcDominant(mat):
    mat = np.matrix(mat)
    newOrder = list(range(len(mat)))
    found = False
    for n in range(len(mat)):
        for m in range(n, len(mat)):
            if (abs(mat[n, m]) > abs(np.sum(mat[n, :]) - mat[n, m])):
                newOrder.pop(m)
                newOrder.insert(n, m)
                found = True
        if not found:
            return None
        mat = mat[:, newOrder]
        newOrder = list(range(len(mat)))
        found=False
    return mat

def calcDominant(mat,b):
    mat = np.matrix(mat)
    newOrder = list(range(len(mat)))
    found = False
    for m in range(len(mat)):
        c = []
        for n in range(m, len(mat)):
            if (abs(mat[n, m]) >= abs(np.sum(mat[n:, m]) - mat[n, m])):
                newOrder.pop(n)
                newOrder.insert(m, n)
                found = True
                break
        if not found:
            return None
        mat = mat[newOrder,:]
        for i in range(len(b)):
            c.append(b[newOrder[i]])
        b = c
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
    mat,y= dominant(mat,y)
    y = gs.gaus(mat, y)
    return y

def polynomial_calc(p, num, pow):
    sum = 0
    for i in range(pow + 1):
        sum = sum + p[i].item(0,0) * (num ** (pow - i))
    return sum

def dominant(mat, b):
    new_mat = StrongcalcDominant(mat)
    if type(new_mat) == type(None):
        new_mat = calcDominant(mat, b)
        if new_mat != None:
           return new_mat
    else:
        return new_mat, b
    return mat, b

if __name__ == "__main__":
    x = [2,1,0]
    b = [-14, -4, 0]

    r = polynomial_approx(x, b)
    print(r)
