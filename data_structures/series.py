import pandas as pd

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