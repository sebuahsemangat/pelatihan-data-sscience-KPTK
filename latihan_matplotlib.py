import matplotlib.pyplot as plt

# Data nilai
nilai = [27, 73, 90, 55, 22, 68, 47, 95, 11, 33, 19, 80, 42, 65, 58, 93, 24, 100,
         35, 13, 86, 48, 66, 37, 14, 75, 18, 39, 60, 44, 21, 16, 92, 88, 50, 72]

# Rentang dan jumlah
label = ['0-25', '26-50', '51-75', '76-100']
jumlah = [0, 0, 0, 0]

# Hitung jumlah sesuai rentang
for n in nilai:
    if n <= 25:
        jumlah[0] += 1
    elif n <= 50:
        jumlah[1] += 1
    elif n <= 75:
        jumlah[2] += 1
    else:
        jumlah[3] += 1

# Gambar grafik batang
plt.bar(label, jumlah)
plt.title('Distribusi Nilai Pemrograman Dasar')
plt.xlabel('Rentang Nilai')
plt.ylabel('Jumlah')

# Tampilkan nilai di atas batang
for i in range(len(jumlah)):
    plt.text(i, jumlah[i], str(jumlah[i]), ha='center')

plt.show()
