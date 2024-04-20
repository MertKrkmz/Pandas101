import pandas as pd
import matplotlib.pyplot as plt

file_path = "sample_data_2.csv"
df = pd.read_csv(file_path)

df.plot(kind='scatter', x='Calisma_Saati', y='Sinav_Notu', color='skyblue', figsize=(10, 6))
plt.title('Çalışma Saati ve Sınav Notu Dağılımı', fontsize=16)
plt.xlabel('Çalışma Saati', fontsize=14)
plt.ylabel('Sınav Notu', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('assets/calisma_saati_sinav_notu_dağılımı.png')