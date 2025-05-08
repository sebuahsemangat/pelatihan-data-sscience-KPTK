# 1. Import pustaka
import numpy as np
from sklearn.linear_model import LinearRegression

# 2. Data jam belajar dan nilai
jam_belajar = np.array([1, 2, 3, 4.5, 5, 6.5, 7, 8, 9, 10])
nilai_ujian = np.array([35, 45, 55, 60, 65, 70, 75, 85, 90, 95])

# 3. Ubah ke bentuk (n,1)
X = jam_belajar.reshape(-1, 1)
y = nilai_ujian

# 4. Buat dan latih model
model = LinearRegression()
model.fit(X, y)

# 5. Input dari pengguna
try:
    input_jam = float(input("Masukkan jam belajar kamu hari ini: "))
    prediksi_nilai = model.predict([[input_jam]])

    # 6. Tampilkan hasil
    print(f"Prediksi nilai ujian kamu: {prediksi_nilai[0]:.2f}")
except ValueError:
    print("Input harus berupa angka.")
