#copy mirip astype tapi tidak harus mengganti type data
import numpy as np
#copy
x = np.array([1,2,3,4])
y = x.copy()
print (x)
print (y)
#copy and replace
a = np.array([
    1,
    2,
    3,
    4,
    ])
b = a.copy()
b[0]=10
print (a)
print (b)
#task
#buatlah indeks short_name berisi nama panggilan seluruh kelas xi A, kemudian copy kedalam array full_name, dan replace dengan nama lengkap semua siswa kelas XI A 

short_name = np.array([
    'Feli',
    'Cang',
    'Wira',
    'Rexx',])

full_name = short_name.copy()
full_name = full_name.astype('O')
full_name[0] = 'Felicia Lovina Cuaca'
full_name[1] = 'Cang Ie Hua'

print (short_name)
print (full_name)