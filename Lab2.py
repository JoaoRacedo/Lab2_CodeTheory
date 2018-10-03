import numpy as np
import sys
import itertools 

#### Functions

'''
Write Matrix with n columns and k rows
@param n (length of code), k (# of basis)
@return Matrix M
'''
def Estandar_G_Matrix(n,k,q):
    Matrix = np.zeros((k,n),dtype=int)
    for i in range(0,k):
        for j in range(0,n):
            Matrix[i][j] = int(input("Fila " + str(i)+ " Columna "+ str(j)+ "\n"))%q
            if(j<k):
                if(i==j):
                    if(Matrix[i][j] != 1):
                        print("Matriz no estandar")
                        return 
                else:
                    if(Matrix[i][j] != 0):
                        print("Matriz no estandar")
                        return 
    return Matrix

'''
Genereate Code C
@param Standar_G_Matrix M, F_{q}^k x
@return return C
'''
def Generate_C(x, q, n, M):
    C = np.zeros((len(x),n), dtype = int)
    for i in range(0,len(C)):
        C[i][:] = x[i].dot(M)%q
    return C

'''
Creates Matrix H
@param Standar_G_Matrix M
@return return H
'''
def Create_H(M,q):
    n = M.shape[1]
    k = M.shape[0]
    #Matrix_I = M[:,range(k)]
    Matrix_P = M[:,range((k),n)]
    P_Transpose = -1*Matrix_P.T
    P_Transpose[P_Transpose < 0] +=q
    Matrix_I = np.identity((n-k), dtype=int)
    H = np.append(P_Transpose,Matrix_I, axis=1)
    return H

'''
Find Min distance of Code C
@param n (length of code), k (# of basis), Matrix_G generator matrix
@return min distance d
'''
def Min_dist(C):
    min = sys.maxsize
    for each in C:
        w = np.count_nonzero(each)
        if(w != 0):
            if (w<min):
                min = w
    return min

'''
Create x vector
@param q (Space), k (# of basis)
@return F_{q}^k
'''
def CreateX(q, k):
    x = np.asarray(list(itertools.product(range(q), repeat = k)))
    return x

'''
Checks if q is prime or not
@param q (Space)
@return True if is , False if not
'''
def IsPrime(q):
    return all(q % i for i in range(2, q))

#### MAIN

# Input n
n = int(input("length of code (n) \n"))
while (n <2 or n >50):
    print("input not valid")
    n = int(input("length of code (n) \n"))

# Input k
k = int(input("number of basis (k) \n"))
while (k<1):
    print("input not valid")
    k = int(input("number of basis (k) \n"))

# Input q
q = int(input("Space (q) \n"))
while (not IsPrime(q)):
    print("q is not odd")
    q = int(input("Space (q) \n"))

# Call of functions
Matrix = Estandar_G_Matrix(n, k, q)
x = CreateX(q,k)
C = Generate_C(x,q,n,Matrix)
min_D = Min_dist(C)
H = Create_H(Matrix,q)

# Show in Terminal
print("The standar G Matrix is:")
print(Matrix)
print(" ")
print("F_{q}^k is:")
print(x)
print(" ")
print("The Code C is:")
print(C)
print(" ")
if(min_D<8):    
    print("The min distance of C is:")
    print(min_D)
    print("The Control Matrix H is:")
    print(H)
else:
    print("The min distance is grater than 7 so the process is going to end")
    print(min_D)





