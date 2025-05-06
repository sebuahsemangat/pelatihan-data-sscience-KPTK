import numpy as np

# Check the version
# print(np.__version__)

# menghitung rata-rata, nilai maksimum, dan nilai minimum dari sebuah array

# Data nilai siswa
# nilai_siswa = np.array([85, 90, 78, 92, 88, 76, 95])

# # Hitung statistik dasar
# rata_rata = np.mean(nilai_siswa)
# maksimum = np.max(nilai_siswa)
# minimum = np.min(nilai_siswa)

# # Tampilkan hasil
# print("Data Nilai Siswa:", nilai_siswa)
# print("Rata-rata Nilai:", rata_rata)
# print("Nilai Tertinggi:", maksimum)
# print("Nilai Terendah:", minimum)

# a2 = np.array([[1,2.0,3.3],
#                [4,5,6.5]])
# print (a2[1][2])

# Array 3Dimensi
a3 = np.array([[[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]])

print(a3[1][2][1])