import pandas as pd
import numpy as np

obje = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e']) # indexli elemanlar
print(obje)
print(obje['b']) # 'b' indexli eleman
print(obje[2:4]) # 2. ve 3. elemanlar
obje["a":"c"] = 10 # 'a', 'b' ve 'c' indexli elemanların değerleri 10 olur.
print(obje)


data = pd.DataFrame(np.arange(16).reshape((4, 4)), 
                    index=['Ankara', 'İstanbul', 'İzmir', 'Bursa'], 
                    columns=['bir', 'iki', 'üç', 'dört']) #  4x4 matris
print(data)

print(data.iloc[1]) # iloc ile 1. satır
print(data.loc['İstanbul']) # loc ile İstanbul satırı
print(data.iloc[1,[1, 2, 3]]) # iloc ile 1. satırın 1., 2. ve 3. sütunları

data[data < 5] = 0 # 5'ten küçük olan elemanlar 0 olur.
print(data)


