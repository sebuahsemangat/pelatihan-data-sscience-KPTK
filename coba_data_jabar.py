import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Contoh memuat ulang data
data = pd.read_csv("data_pengunjung_perpustakaan.csv")

# Tambahkan fitur-fitur tambahan secara acak
np.random.seed(42)
data['jumlah_penduduk'] = np.random.randint(50000, 300000, size=len(data))
data['jumlah_perpustakaan'] = np.random.randint(1, 10, size=len(data))
data['jumlah_sekolah'] = np.random.randint(10, 100, size=len(data))

# Fitur dan target
X = data[['jumlah_penduduk', 'jumlah_perpustakaan', 'jumlah_sekolah']]
y = data['jumlah_pemustaka']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat dan latih model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Tampilkan akurasi
print("Skor akurasi (R^2):", model.score(X_test, y_test))

# Visualisasi prediksi vs nilai aktual
plt.scatter(y_test, y_pred, color='green')
plt.xlabel('Nilai Aktual')
plt.ylabel('Hasil Prediksi')
plt.title('Prediksi Jumlah Pengunjung Perpustakaan')
plt.grid(True)
plt.show()
