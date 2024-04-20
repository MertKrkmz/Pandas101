import pandas as pd

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