
from sympy import *
import numpy as np

r=int(input('No of rows = '))
c=int(input('No of columns = '))
array=[]
for x in range(r):
    a=[]
    print('Row',x)
    for y in range(c):
        print('     Columnn '+str(y),end='= ')
        value=int(input())
        print()
        a.append(value)
    array.append(a)

arr=np.array(array)
print(arr)

# Use sympy.rref() method
M_rref = arr.rref()
	
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
