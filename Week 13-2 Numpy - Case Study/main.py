# nilai kelas X, saya mau tampilkan nilai tertinggi, terendah, rata-rata, median, berapa orang yang lulus

import numpy as np
nilai_siswa = np.array([57,65,76,75,78,89,90])

#max
nilai_tertinggi =np.max(nilai_siswa)
nilai_terendah =np.min(nilai_siswa)
rata_rata = np.mean(nilai_siswa)
nilai_median = np.median(nilai_siswa)
siswa_lulus = np.sum(nilai_siswa >= 75)
siswa_tidak_lulus = np.sum(nilai_siswa < 75)
print("Nilai Tertinggi = ",nilai_tertinggi)
print("Nilai Terendah = ",nilai_terendah)
print("Nilai Rata-Rata = ",rata_rata)
print("Nilai Median = ",nilai_median)
print("Jumlah Siswa Lulus = ",siswa_lulus)

# Hitunglah 
#     a. siswa yang tidak lulus
#     b. persentase siswa lulus 
#     c. persentase siswa yang tidak lulus

persentase_lulus = (siswa_lulus/len(nilai_siswa))*100
print(persentase_lulus)
persentase_tidak_lulus = (siswa_tidak_lulus/len(nilai_siswa))*100
print(persentase_tidak_lulus)