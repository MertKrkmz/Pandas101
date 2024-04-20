import matplotlib.pyplot as plt
import pandas as pd

file_path = "sample_data_1.csv" # csv dosyasının yolu
data = pd.read_csv(file_path) # csv dosyasını oku

#--------------------------------------------
# Yaşa göre maaşların ortalamasını hesaplayın
yas_maas_ortalamasi = data.groupby('yas')['maas'].mean()

# Çizgi grafiği çizin
plt.figure(figsize=(10, 6))  # Grafik boyutunu belirleyin
plt.plot(yas_maas_ortalamasi.index, yas_maas_ortalamasi.values, marker='o', color='skyblue', linestyle='-', linewidth=2, markersize=8) # Çizgi grafiğini çizin

# Grafik başlığını ve etiketlerini ayarlayın
plt.title('Yaşa Göre Maaş Ortalaması', fontsize=16)
plt.xlabel('Yaş', fontsize=14)
plt.ylabel('Maaş Ortalaması', fontsize=14)

# Eksen etiketlerinin font büyüklüğünü ve stilini ayarlayın
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Grid çizgilerini ekleyin
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Grafik alanını hafifçe büyütün
plt.tight_layout()

# Grafik dosyasını kaydedin
plt.savefig('assets/yasa_gore_maas_ortalamasi.png')