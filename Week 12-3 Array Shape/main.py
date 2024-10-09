import numpy as np

arr = np.array([1,2,3,4,5])
print_shape = arr.shape

arr = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print_shape = arr.shape

print (print_shape)

#array reshape
#mengubah bentuk array kedalam dimensi yagn lain

#reshape 1d to 2d
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)



