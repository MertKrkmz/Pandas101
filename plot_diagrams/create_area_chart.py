import pandas as pd
import numpy as np

# Örnek zaman serisi verisi oluşturalım (30 gün)
tarihler = pd.date_range(start='2024-01-01', periods=30)
sicaklik = np.random.randint(10, 30, size=30)

# DataFrame oluşturalım
veri = pd.DataFrame({'Tarih': tarihler, 'Sicaklik': sicaklik})

print(veri.head())

import matplotlib.pyplot as plt



plt.figure(figsize=(10, 6))
plt.fill_between(veri['Tarih'], veri['Sicaklik'], color='skyblue', alpha=0.4) # Dolgu rengi ekler.

plt.plot(veri['Tarih'], veri['Sicaklik'], color='blue', alpha=0.6) # Çizgi grafiğini çizer.

plt.title('Günlük Sıcaklık Değişimi')
plt.xlabel('Tarih')
plt.ylabel('Sıcaklık (°C)')
plt.xticks(rotation=60)
plt.grid(True) # Grid çizgisi ekler.

plt.tight_layout()
plt.savefig('assets/gunluk_sicaklik_degisimi.png')