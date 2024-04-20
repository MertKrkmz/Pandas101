import pandas as pd
import numpy as np

# Örnek veri setini oluşturalım
np.random.seed(42)  # Rastgeleliğin tekrarlanabilir olması için seed değerini ayarlayalım

# Öğrenci sayısı
ogrenci_sayisi = 100

# Rastgele çalışma saatleri oluşturalım (1 ile 10 arasında)
calisma_saatleri = np.random.randint(1, 11, size=ogrenci_sayisi)

# Her bir çalışma saati için rastgele sınav notu oluşturalım (0 ile 100 arasında)
sinav_notlari = np.random.randint(0, 101, size=ogrenci_sayisi)

# Oluşturulan verileri bir DataFrame'e dönüştürelim
data = pd.DataFrame({
    'Calisma_Saati': calisma_saatleri,
    'Sinav_Notu': sinav_notlari
})
print(data)

# Korelasyon matrisini hesaplayalım
correlation_matrix = data.corr()

# Korelasyon matrisini yazdıralım
print("Korelasyon Matrisi:")
print(correlation_matrix)

# Çalışma saati ile sınav notu arasındaki korelasyonu yazdıralım
calisma_saat_sinav_korelasyonu = correlation_matrix.loc['Calisma_Saati', 'Sinav_Notu']
print("\nÇalışma Saati ve Sınav Notu Arasındaki Korelasyon:", calisma_saat_sinav_korelasyonu)

""" Calisma_Saati ile Sinav_Notu arasındaki korelasyon katsayısı -0.0435'tir. 
Bu değer neredeyse sıfıra yakındır. Bu, çalışma saati ile sınav notu arasında çok zayıf bir negatif ilişki olduğunu gösterir. 
Yani, çalışma saati arttıkça, sınav notu genellikle düşmez veya yükselmez. """
