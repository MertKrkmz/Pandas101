import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Rastgele veri oluşturma
np.random.seed(0)
aylar = ['Şubat']
imagine = np.random.randint(2000, 5001, size=1)
upscaler = np.random.randint(2000, 5001, size=1)
repeater = np.random.randint(2000, 5001, size=1)

# Verileri bir DataFrame'e yerleştirme
df = pd.DataFrame({'Ay': aylar, 'Imagine': imagine, 'Upscaler': upscaler, 'Repeater': repeater})


# 'Şubat' ayının kullanım pasta grafiği
subat_veri = df[df['Ay'] == 'Şubat'].iloc[:, 1:]  # 'Şubat' ayına ait veriyi seçme
plt.figure(figsize=(10, 6))
plt.pie(subat_veri.values.flatten(), labels=subat_veri.columns, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Daireyi mükemmel bir daire yapar.
plt.title('Şubat Ayı Kullanımı')
plt.tight_layout()
plt.savefig('assets/subat_kullanim.png')