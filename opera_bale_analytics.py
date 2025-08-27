# -*- coding: utf-8 -*-
# Opera & bale veri analizi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

# CSV dosyasından veri yükleme ve sütun isimlerini belirleme
columns_opera = [
    "Sezon yılı",
    "Opera ve bale salonu",
    "Koltuk sayısı",
    "bos1",
    "Toplam oynanan eser sayısı",
    "Oynanan yerli eser",
    "Oynanan yabancı eser",
    "bos2",
    "Toplam seyirci sayısı",
    "Yerli eser seyirci sayısı",
    "Yabancı eser seyirci sayısı"
]

df_opera = pd.read_csv("/Users/deryagokdagli/Desktop/myPythonProjects/Projem/opera.csv",
                       skiprows=4, names=columns_opera)

# Boş değerleri kontrol etme
print(f"Boş değer sayısı:\n{df_opera.isnull().sum()}")

# Veri çerçevesinin ilk ve son 5 satırı
print(f"İlk 5 satır:\n{df_opera.head()}")
print(f"Son 5 satır:\n{df_opera.tail()}")

# Yeterli veri olmayan satırları ve tamamen boş sütunları kaldırma
df_opera.dropna(thresh=2, inplace=True)
df_opera.dropna(axis=1, how="all", inplace=True)

# Veri çerçevesini görüntüleme
print(f"Temizlenmiş veri:\n{df_opera}")

# Temel istatistikler
print(f"Opera & Bale Temel İstatistikler:\n{df_opera.describe()}")

# - - - - - - - - - - - - 
x = df_opera["Sezon yılı"]
y_yerli = df_opera["Yerli eser seyirci sayısı"]
y_yabanci = df_opera["Yabancı eser seyirci sayısı"]

plt.figure(figsize=(8,4), dpi=100)

plt.plot(x, y_yerli, marker="o", color="#3E87AB", label="Yerli Eser Seyirci")
plt.plot(x, y_yabanci, marker="s", color="#FF7F50", label="Yabancı Eser Seyirci")

plt.title("Opera & Bale: Sezonlara Göre Seyirci Trendleri (2000–2024)", fontsize=14)
plt.xlabel("Sezon yılı", fontsize=12)
plt.ylabel("Seyirci Sayısı", fontsize=12)
plt.xticks(rotation=45) 
plt.grid(alpha=0.2)
plt.legend()

plt.tight_layout()
plt.show()

# - - - - - - - - - - - - 
x = df_opera["Sezon yılı"]
y_oynananyerli = df_opera["Oynanan yerli eser"]
y_oynananyabanci = df_opera["Oynanan yabancı eser"]
plt.figure(figsize=(8,4), dpi=100)

plt.plot(x, y_oynananyerli, label="Oynanan yerli eser", marker="o", color="#F4D35E")
plt.plot(x, y_oynananyabanci, label="Oynanan yabancı eser", marker="s", color="#4361EE")
plt.title("Opera & Bale: Oynanan Yerli ve Yabancı Eser Sayılarının Dağılımı")
plt.xlabel("Sezon yılı",fontsize=12)
plt.ylabel("Yerli & Yabancı Eser",fontsize=12)
plt.xticks(rotation=45)
plt.grid(alpha=0.2)
plt.legend()

plt.tight_layout()
plt.show()

# - - - - - - - - - - - - 
x_yerliesersayisi = df_opera["Oynanan yerli eser"]
y_yerlieserizleyici = df_opera["Yerli eser seyirci sayısı"]

plt.figure(figsize=(8,4), dpi=100)

plt.scatter(x_yerliesersayisi, y_yerlieserizleyici, marker="o", label="Oynanan yerli eser")

plt.xlabel("Yerli Eser Sayısı")
plt.ylabel("Yerli Eser Seyirci Sayısı")
plt.title("Opera & Bale: Yerli Eser Sayısı vs Seyirci Sayısı")
plt.legend()

plt.tight_layout()
plt.show()
s = df_opera["Oynanan yerli eser"].corr(df_opera["Yerli eser seyirci sayısı"])
print(f"Opera & Bale: Yerli Eser Sayısı vs Seyirci Sayısı tablosunun korelasyonu: {s}")

# - - - - - - - - - - - - 
x_yabanciesersayisi = df_opera["Oynanan yabancı eser"]
y_yabancieserizleyici = df_opera["Yabancı eser seyirci sayısı"]

plt.figure(figsize=(8,4), dpi=100)

plt.scatter(x_yabanciesersayisi, y_yabancieserizleyici, marker="s", label="Oynanan yabancı eser")
plt.xlabel("Yabancı Eser Sayısı")
plt.ylabel("Yabancı Eser Seyirci Sayısı")
plt.title("Opera & Bale: Yabancı Eser Sayısı vs Seyirci Sayısı")
plt.legend()

plt.tight_layout()
plt.show()
r = df_opera["Oynanan yabancı eser"].corr(df_opera["Yabancı eser seyirci sayısı"])
print(f"Opera & Bale: Yabancı Eser Sayısı vs Seyirci Sayısı tablosunun korelasyonu: {r}")

# - - - - - - - - - - - - 
x_koltuk = df_opera["Koltuk sayısı"]
y_yerli = df_opera["Yerli eser seyirci sayısı"]
y_yabanci = df_opera["Yabancı eser seyirci sayısı"]

plt.figure(figsize=(8,4), dpi=100)

plt.scatter(x_koltuk, y_yerli, color="#636EFA", marker="o", label="Yerli Eser Seyirci", s=100,alpha=0.8)
plt.scatter(x_koltuk, y_yabanci, color="#EF553B", marker="s", label="Yabancı Eser Seyirci", s=100,alpha=0.8)

plt.title("Opera & Bale: Yerli-Yabancı Eser Seyirci ve Koltuk Dağılımı (2000–2024)", fontsize=14)
plt.xlabel("Koltuk sayısı", fontsize=12)
plt.ylabel("Seyirci Sayısı", fontsize=12)
plt.grid(alpha=0.2)
plt.legend()

plt.tight_layout()
plt.show()
t1 = df_opera["Koltuk sayısı"].corr(df_opera["Yerli eser seyirci sayısı"])
t2 = df_opera["Koltuk sayısı"].corr(df_opera["Yabancı eser seyirci sayısı"])
print(f"Koltuk sayısı ↔ Yerli seyirci korelasyonu: {t1:.2f}")
print(f"Koltuk sayısı ↔ Yabancı seyirci korelasyonu: {t2:.2f}")


