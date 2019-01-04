import numpy as np
import sor

def newLine(points, l, i):
    l[i-1] = 1/6 *(points[i][0] - points[i - 1][0])
    l[i] = 1 / 3 * (points[i][0] - points[i - 1][0] + points[i + 1][0] - points[i][0])
    l[i + 1] = 1 / 6 * (points[i + 1][0] - points[i][0])
    return l

def create_b(points, i):
    return (points[i+1][1] - points[i][1])/ (points[i+1][0] - points[i][0]) - (points[i][1] - points[i - 1][1])/ (points[i][0] - points[i - 1][0])

def create_Si(points, M, i, x):
    yi_plus_1 = points[i + 1][1]
    yi = points[i][1]
    hi = points[i + 1][0] - points[i][0]
    x_minus_xi = x - points[i][0]
    x_minus_xi1 = x - points[i + 1][0]

    a1 = (yi_plus_1 * x_minus_xi)/hi
    a2 = (yi * x_minus_xi1)/hi
    a3 = (M[i+1]/6)
    a4 = (x_minus_xi ** 3)/hi - hi * x_minus_xi
    a5 = (M[i]/6)
    a6 = (x_minus_xi1**3)/hi - hi * x_minus_xi1
    return a1 - a2 - a3 *a4 - a5 * a6

def spline(points, x):
    sum = 0
    mylist = []
    b = [0 for i in range(len(points))]
    l = [0 for i in range(len(points))]
    l[0] = 1
    mylist.append(l)

    for j in range(0, len(points) - 1):
        mylist.append([0 for i in range(len(points))])
    mylist[len(mylist) - 1][len(points) - 1] = 1

    for i in range(1, len(points) - 1):
        mylist[i] = newLine(points, mylist[i], i)

    for i in range(1, len(b) - 1):
        b[i] = create_b(points, i)

    mylist = np.matrix(mylist)
    result = sor.SOR(mylist, b)

    for i in range(len(points) - 1):
        sum += create_Si(points, result, i, x)
    return sum


print(spline([(1,1), (2, 2), (3, 1), (4,1.5), (5,1)], 1.5))
