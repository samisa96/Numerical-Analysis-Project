from Bisection_method.py import *
from NewtonRephson.py import *
from math import sqrt

def Find_Rij(point_i,point_j,h):
    return sqrt(((point_i[0]-point_j[0])**2)+((point_i[1]-point_j[1])**2)+(h**2))
def Calculate_Dij(c,k,u,h,point_i,point_j):
    return (c*(1+k*h)*exp(-u*Distance_Rij(point_i,point_j,h)))/(Distance_Rij(point_i,point_j,h)**2)
def Find_c(func):
    roots1=