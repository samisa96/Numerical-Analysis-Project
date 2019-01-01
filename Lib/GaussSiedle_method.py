import numpy as np

def iterative(matrix, b, c, printList):
    result = []
    sum = 0
    count = 0
    k = 0
    flag = 0
    flag2 = 0

    for i in range(len(matrix)):
        result.append(0)

    while(flag2 == 0 and count <= 100):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                sum = sum + (matrix.item(i, j)*result[j])
            sum = sum + c[i]
            if  b[i] > 0.001:
                sum = sum / b[i]
            if abs(sum - result[i]) > 0.0000001:
                flag = 1
            result[i] = sum
            sum = 0

        if flag == 0:
            flag2 = 1
        else:
            flag = 0
        count = count + 1
        printList.append(count)
        for j in result:
            printList.append(j)

    return result

def is_close(line, b, result, eps):
    sum = 0
    for i in range(line.getA().size):
        sum = sum +(result[i] * line.item(0,i))
    if abs(sum - b) < eps:
        return True
    return False

def sum_m(mat1, mat2):
        result = []

        for i in range(len(mat1)):
            mylist = []
            for j in range(len(mat2)):
                mylist.append(0.0)
            result.append(mylist)

        mat = np.matrix(result)

        for i in range(len(mat1)):
            for j in range(len(mat2)):
                mat.itemset((i, j), (mat1.item(i, j) + mat2.item(i, j)))

        new_mat = np.matrix(mat)
        return new_mat

def multi_m(mat1, mat2):
    result = []

    for i in range(len(mat1)):
        mylist = []
        for j in range(len(mat1)):
            mylist.append(0.0)
        result.append(mylist)

    mat = np.matrix(result)

    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1)):
                mat.itemset((i, j), (mat1.item(i, k) + mat2.item(k, j)))

    new_mat = np.matrix(mat)
    return new_mat

def multi_scalar(mat, num):
    result = []

    for i in range(len(mat)):
        mylist = []
        for j in range(len(mat)):
            mylist.append(mat.item(i, j) * num)
        result.append(mylist)

    new_mat = np.matrix(result)
    return new_mat

def create_D(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i == j:
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    D = np.matrix(result)
    return D

def create_L(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i > j:
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    L = np.matrix(result)
    return L

def create_U(matrix):
    result = []
    for i in range(len(matrix)):
        m = []
        for j in range(len(matrix)):
            if i < j:
                m.append(float(matrix.item(i, j)))
            else:
                m.append(0.0)
        result.append(m)
    U = np.matrix(result)
    return U

def PrintList(printList):
    for i in range(0 ,len(printList)-1, 4):
        print("number iteration:", printList[i])
        for j in range(1 , 4):
            print("x", j, ": ", printList[i + j])

def gaus(matrix, b):
    D = create_D(matrix)
    L = create_L(matrix)
    U = create_U(matrix)

    L_D = sum_m(L, D)
    L_D_INVERSE = (L_D.I)
    L_D_U = np.matmul(L_D_INVERSE, U)
    L_D_b = np.matmul(L_D_INVERSE, b)
    L_D_U_1 = multi_scalar(L_D_U,-1)

    new_b = []
    for i in range(len(b)):
        new_b.append(1.0)

    L_D_b = L_D_b.getA()[0]

    printList = []
    r = iterative(L_D_U_1, new_b ,L_D_b, printList)
    PrintList(printList)
    return r


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
        found = False
    return mat,b

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
    # Example:
    mat = np.matrix([[1, 3, 5], [1, 4, 2], [5, 2, 9]])
    b = [1, 2, 3]
    # Example:
    '''mat = np.matrix([[2, 3, 5], [1, 5, 2], [7, 2, 3]])
    b = [1, 2, -2]'''
    # Example:
    '''mat = np.matrix([[1, 3, 5], [6, 5, 2], [7, 1, 3]])
    b = [1, 3, -2]'''
    # Example:
    '''mat = np.matrix([[1, 3, 5], [1, 1, 2], [3, 2, 3]])
    b = [1, 2, -2]'''
    # Example:
    '''mat = np.matrix([[1, 1, 1], [2, 1, 2], [4, 2, 3]])
    b = [1, 2, -2]'''
    # Example:
    '''mat = np.matrix([[1, 0, 1], [2, 1, 2], [4, 2, 3]])
    b = [1, 2, -2]'''

    r = dominant(mat, b)
    mat = r[0]
    b = r[1]

    print(gaus(mat, b))
