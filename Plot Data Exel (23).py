import pandas as pd
import matplotlib.pyplot as plt
# Membaca file Excel
file_path = r"C:\Users\attala\Documents\Attala Muflih Gumilang\S1 Fisika UIN Bandung Sunan Gunung Djati\Semester 5\Prak Fiskom\Tugas 3\data1.xlsx"
data = pd.read_excel(file_path)
# Asumsi bahwa kolom pertama adalah X dan kolom kedua adalah Y
X = data.iloc[:, 0] # Kolom pertama (nilai sumbu x)
Y = data.iloc[:, 1] # Kolom kedua (nilai sumbu y)
# Plotting data
plt.plot(X, Y)
plt.title('Data dari "data1.xlsx"')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
