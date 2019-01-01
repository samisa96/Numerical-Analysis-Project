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

def polynomial_approx(vector_x, vector_y, x):
    mat = []
    row = []
    sum = 0
    for j in range(len(vector_x)):
        for i in range(len(vector_x)):
            z = lambda vector_y : vector_y ** (len(vector_x) -i - 1)
            row.append(z(vector_x[j]))
        mat.append(row)
        row = []
    mat = np.matrix(mat)
    mat,vector_y= dominant(mat,vector_y)
    coefficients = gs.gaus(mat, vector_y)
    print('The possession of the polynomial is :', len(coefficients))
    for i in range(len(coefficients)):
        print('Coefficient for x^',len(coefficients) - 1 - i,'is : ', coefficients[i])
        sum += coefficients[i] * (x ** (len(coefficients) - 1 - i))
    return sum

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
    #vector x = [-7,1,-0.2]
    #vector y = [2,8.8, 0.7]
    # example result 12.91241

    #vector_x = [0,1.5,-5,2,5]
    #vector_y = [2,6,4,2,5]
    #example result 6.3722
    x = [0,1.5,-5,2,5]
    y = [2,6,4,2,5]
    r = polynomial_approx(x, y,0.5)
    print(r)
