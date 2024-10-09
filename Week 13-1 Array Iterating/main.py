import numpy 
np = numpy

arr = np.array([1,2,3])

for x in arr:
    print(x)


arr2d = np.array([[1,2,3],[4,5,6]])
#matrix element (baris dan kolom)
for x in arr2d:
    print(x)

#scalar element (satu kolom)
for x in arr2d:
    for y in x:
        print(y)

#buatlah Array 2 dimensi berisi bilangan bulat [1..20]
# kemudian buatlah tampilan scalar dan matrix nya
