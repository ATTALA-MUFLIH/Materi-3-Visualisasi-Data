import numpy as np
import matplotlib.pyplot as plt


g = 9.8  
h0 = float(input("Masukkan ketinggian awal (h0) dalam meter: "))

t_fall = np.sqrt((2 * h0) / g)
print(f"Waktu yang diperlukan untuk mencapai tanah: {t_fall:.2f} detik")

t = np.linspace(0, t_fall, num=500)

v = g * t

h = h0 - (0.5 * g * t**2)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(t, v, label="Kecepatan (v)", color='b')
plt.title("Grafik Kecepatan vs Waktu")
plt.xlabel("Waktu (s)")
plt.ylabel("Kecepatan (m/s)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(t, h, label="Ketinggian (h)", color='g')
plt.title("Grafik Ketinggian vs Waktu")
plt.xlabel("Waktu (s)")
plt.ylabel("Ketinggian (m)")
plt.grid(True)

plt.tight_layout()
plt.show()
