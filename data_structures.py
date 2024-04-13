import pandas as pd
import matplotlib.pyplot as plt

# Series tipi veri yapısı
# Series tipi, tek boyutlu bir veri yapısıdır.
data = pd.Series(["mert", 7, -5, 3]) # index verilmezse default olarak 0, 1, 2, 3, ... şeklinde indexler atanır.
print(data) 
print("data[0] = ", data[0]) # 0. eleman
print("array = ", data.values) # array
print("index = ", data.index) # index

data = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"]) # index verilirse verilen indexler atanır.
print(data) # indexli elemanlar
print("data['a'] = ", data["a"]) # 'a' indexli eleman
print("index = ", data.index) # index 

# Series tipi veri yapısı
points = {"A": 10, "B": 20, "C": 30, "D": 40} # dictionary
data = pd.Series(points) # dictionary'den series oluşturulabilir.
print(data) 
print("data['A'] = ", data["A"]) # 'A' indexli eleman
print(data>20) # 20'den büyük olanlar True, diğerleri False
print(data[data>20]) # 20'den büyük olan elemanlar
data["A"] = 100 # 'A' indexli elemanın değeri değiştirilebilir.
print(data)
data[data<32] = 43 # 30'dan küçük olan elemanların değeri değiştirilebilir.
print(data)
print("E" in data) # 'A' indexli eleman var mı?
data = data**2 # her elemanın karesi alınır.
print(data)
print(data.isnull()) # NaN olanlar True, diğerleri False """

# DataFrame tipi veri yapısı
# DataFrame tipi, iki boyutlu bir veri yapısıdır.
dosya_yolu = "sample_data.csv" # csv dosyasının yolu
data = pd.read_csv(dosya_yolu) # csv dosyasını oku
print(data)
print(data.dtypes) # her sütunun veri tipi 
print(data.maas.describe()) # maas sütununun istatistiksel bilgileri
#count = kaç tane eleman var
#mean = ortalama
#std = standart sapma
#min = minimum değer
#25% = 1. çeyrek değer
#50% = medyan değer
#75% = 3. çeyrek değer
#max = maksimum değer
print(data.isim.describe()) # isim sütununun istatistiksel bilgileri
#count = kaç tane eleman var
#unique = kaç farklı eleman var
#top = en çok tekrar eden eleman
#freq = en çok tekrar eden elemanın sayısı
print(data.value_counts()) # her sütundaki elemanların kaç tane olduğu
print(data.yas.value_counts()) # yas sütunundaki elemanların kaç tane olduğu
print(data.maas.value_counts(normalize=True)) # maas sütunundaki elemanların yüzdelik dilimleri
print(type(data.isim.value_counts())) # type = Series
print(data.isim.value_counts().head()) #Series olduğu için head() fonksiyonu kullanılabilir.
print(data.isim.unique()) # isim sütunundaki farklı elemanlar
print(data.isim.nunique()) # isim sütunundaki farklı eleman sayısı
print(pd.crosstab(data.yas, data.maas)) # yas ve maas sütunları arasındaki ilişki

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

#--------------------------------------------
# Veri setindeki sütunları seçme
data = pd.DataFrame(data, columns=['isim', 'yas', 'maas']) # sadece isim, yas ve maas sütunlarını al
print(data)

# Veri setindeki sütunları seçme ve yeni bir sütun eklemek
data = pd.DataFrame(data, columns=['isim', 'yas', 'maas', 'sehir']) # sehir sütunu yok, bu yüzden NaN değerler atanır.
print(data)
data.loc[:, 'sehir'] = 'Ankara' # sehir sütununa 'Ankara' değerini ata
print(data)
# satır seçme
print(data.loc[0]) # 0. satır
print(data.loc[0:2]) # 0. satırdan 2. satıra kadar
print(data.loc[0:2, 'isim']) # 0. satırdan 2. satıra kadar isim sütunu
print(data.loc[0:2, ['isim', 'yas']]) # 0. satırdan 2. satıra kadar isim ve yas sütunları

del data['sehir'] # sehir sütununu sil
print(data)