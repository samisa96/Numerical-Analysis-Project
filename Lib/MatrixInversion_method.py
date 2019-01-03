def transposeMatrix(m):
    """returns list object of the transpose matrix"""
    return list(map(list,zip(*m)))

def getMatrixMinor(m,i,j):
    """calculate the minor when you drop line i  and column j"""
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    """function to calculate the deternminant if the matrix is not square print a massage else return the deternminant"""
    #base case for 2x2 matrix
    if len(m) == 2:
        if len(m[0])==2 and len(m[1])==2:
          return m[0][0]*m[1][1]-m[0][1]*m[1][0]
        else:
            print("not square matrix")
            return
    flag=0
    determinant = 0
    for i in m:
        if len(i)!=len(m):
            flag=1
    if flag==0:
        for c in range(len(m)):
          determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
        return determinant
    else:
       print("not square matrix")
       return

def getMatrixInverse(m):
  determinant = getMatrixDeternminant(m)
  if determinant!=None:
     print("the deternminant of the matrix is {} so there's inverse matrix:".format(determinant))
     #special case for 2x2 matrix:
     if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

#find matrix of cofactors
     cofactors = []
     for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
     cofactors = transposeMatrix(cofactors)
     for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            if determinant !=0:
              cofactors[r][c] = cofactors[r][c]/determinant
            else:
              return'inversion matrix doesnt exist'
     return cofactors
  else:
     return


  '''
m=[[5,2,1,0],[0,1,2,0],[0,3,1,0],[0,0,0,1]]
print(getMatrixInverse(m))  '''