import numpy as np
arr = np.array([1,2,3,4,5,6,7])

#slicing between bottom and top index
slicing = arr[1:5]
print(slicing)

#slicing from bottom to end
slicing = arr[4:] #array ke 4 nya masuk
print(slicing)

#slicing from top to start 
slicing = arr[:4] #array ke 4 nya tidak masuk
print(slicing)

#tampilkan array [0] sampai [3]  kemudian tampikan array [5]sampai [6] tampilan keduanya digabung dalam satu baris