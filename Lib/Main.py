import Bisection_method
import NewtonRephson_method
import Secant_method
import Poly_aprox as pa
import GaussSiedle_SOR as gsor
from sympy import *
from numpy import matrix
from math import sqrt

def Find_Rij(point_i,point_j,h):
    return sqrt(((point_i[0]-point_j[0])**2)+((point_i[1]-point_j[1])**2)+(h**2))

def Calculate_Dij(c,k,u,h,point_i,point_j):
    return (c*(1+k*h)*exp(-u*Find_Rij(point_i,point_j,h)))/(Find_Rij(point_i,point_j,h)**2)

def Find_Roots(func):
    ranging = Bisection_method.intervals(-100, 100, 0.5)
    fx = lambdify(x, func)
    fx_tag=Bisection_method.derivative(func)
    roots1=Bisection_method.all_roots(ranging, fx, fx_tag, 100, 0.001)
    roots2=Secant_method.all_roots(fx, 0.001, [-100,100], 100)
    if roots1==None or roots2==None or len(roots1)!=len(roots2):
        return "Error"
    for i in range(len(roots1)):
        if(roots1[i] - roots2[i] > 0.001 ):
            return "Error"
    return roots1

def Find_c(func):
    roots=Find_Roots(func)
    final_roots=[]
    sum = 0
    for n in roots:
        if n>0:
            final_roots.append(n)
            sum+=n
    if(len(final_roots) == 0):
        return "Error"
    return sum / len(final_roots)

def Find_k(vector_x,vector_y,num):
    polynom = pa.polynomial_approx(vector_x, vector_y)
    return pa.polynomial_calc(polynom, num, len(polynom) - 1)

def Find_u(func):
    roots = Find_Roots(func)
    if roots == None:
        return "No roots"
    return roots[0]/100

def Calculate_D(step_size,c,k,u,h):
    matrix_D = []
    points=[[0,0],[step_size,0],[0,step_size],[step_size,step_size]]
    for point_i in points:
        tmp = []
        for point_j in points:
            tmp.append(Calculate_Dij(c,k,u,h,point_i,point_j))
        matrix_D.append(tmp)
    return matrix(matrix_D)

def Calculate_Vector_C(matrix_D,vector_M):
    return gsor.gaus(matrix_D,vector_M) and gsor.SOR(matrix_D,vector_M)


if __name__ == '__main__':
    x = Symbol('x')
    Fx = 16*x**3-16*x**2+1
    c = Find_c(Fx)

    vector_x = [1, 3, 5]
    vector_y = [10.5, 6.1, 3.5]
    k = Find_k(vector_x, vector_y, 4.74)

    Fx = x*exp(-x)-0.25
    u = Find_u(Fx)

    h = 200
    step_size=100
    matrix_D = Calculate_D(step_size,c,k,u,h)

    vector_M = [900,950,1000,1100]
    vector_C = Calculate_Vector_C(matrix_D,vector_M)
    print(vector_C)