#Representasi Data Type di numpy berbeda 
# i = integer 
# b = boolean
# u = unsigned integer (integer positif 10), sign (negatif -10)
# f = float 
# c = complex float
# m = time delta
# M = date time
# O = object
# S = string
# U = unicode string
# V = void 
# paramater Feli adalah manusia, bernafas

import numpy as np
arr = np.array([-1,-2,-3,-4]) 
#() parameter [] array object
check = arr.dtype
print(check)

arrkedua = np.array(['Shane','Cang Ie Hua', 'Wira'])
check= arrkedua.dtype
print(check)

arr = np.array([ 1.1, 2.1, 3.1, 4.1]) 
#() parameter [] array object
check = arr.dtype
print(check)

#Define data_type before check
arr = np.array([1,2,3,4], dtype='S')
check = arr.dtype
print(check, arr)

arr = np.array([1,2,3,4], dtype='f')
check = arr.dtype
print(check)
#rules string cannot be change into integer,
#string "1", string "Vincent"

#define and copy new array
arr= np.array([1,2,3,4])
arrbaru = arr.astype(float)
print(arr, arrbaru)