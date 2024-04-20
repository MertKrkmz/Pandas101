import pandas as pd
import matplotlib.pyplot as plt

file_path = "sample_data.csv" # csv dosyasının yolu
data = pd.read_csv(file_path) # csv dosyasını oku

#--------------------------------------------
# Histogram çizimi
plt.figure(figsize=(10, 6))  # Grafik boyutunu belirleyin
plt.hist(data['maas'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)  # Histogramı çizin

# Grafik başlığını ve etiketlerini ayarlayın
plt.title('Maaş Dağılımı', fontsize=16)
plt.xlabel('Maaş', fontsize=14)
plt.ylabel('Frekans', fontsize=14)

# Eksen etiketlerinin font büyüklüğünü ve stilini ayarlayın
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Grid çizgilerini ekleyin
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafik alanını hafifçe büyütün
plt.tight_layout()

plt.savefig('assets/maas_histogram.png')    