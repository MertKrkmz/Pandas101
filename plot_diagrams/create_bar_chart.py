import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Rastgele veri oluşturma
np.random.seed(0)
aylar = ['Ocak', 'Şubat', 'Mart']
imagine = np.random.randint(2000, 5001, size=3)
upscaler = np.random.randint(2000, 5001, size=3)
repeater = np.random.randint(2000, 5001, size=3)

# Verileri bir DataFrame'e yerleştirme
df = pd.DataFrame({'Ay': aylar, 'Imagine': imagine, 'Upscaler': upscaler, 'Repeater': repeater})

# Bar grafiği çizimi
df.plot(kind='bar', x='Ay', figsize=(10, 6))

plt.xlabel('Ay')
plt.ylabel('Kullanım Sayısı')
plt.title('Aylık Imagine, Upscaler ve Repeater Kullanımı')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('assets/aylik_kullanim.png')


# 'Şubat' ayının kullanım pasta grafiği
subat_veri = df[df['Ay'] == 'Şubat'].iloc[:, 1:]  # 'Şubat' ayına ait veriyi seçme
plt.figure(figsize=(10, 6))
plt.pie(subat_veri.values.flatten(), labels=subat_veri.columns, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Daireyi mükemmel bir daire yapar.
plt.title('Şubat Ayı Kullanımı')
plt.tight_layout()
plt.savefig('assets/subat_kullanim.png')
