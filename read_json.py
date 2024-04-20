import pandas as pd

#import json file 
file_path = "sample_data.json" 
df = pd.read_json(file_path) # read json file

print(df.to_string()) 

print(df.tail()) # last 5 rows
print(df.head()) # first 5 rows
print(df.info()) # information about the data
print(df.describe()) # summary statistics of the data
print(df.shape) # number of matrix rows and columns count
print(df.columns) # column names
print(df.index) # index range
print(df.dtypes) # data types of each column

#--------------------------------------------
# remove null rows
df.dropna(inplace=True) # dropna(inplace=True) method removes the null rows from the original dataframe
print(df.to_string())

#--------------------------------------------
df = pd.read_json(file_path) # read json file
# fill null rows
df.fillna(999, inplace=True) # fillna() method fills the null rows with the given value
print(df.to_string())

#--------------------------------------------
# mean(), median(), mode(), std(), var(), sum(), min(), max() functions
x = df["Calories"].mean() 
print("average value: ", x)
x = df["Calories"].median()
print("median value: ", x)
x = df["Calories"].mode()
print("mode value: ", x)
x = df["Calories"].std()
print("standard deviation value: ", x)
x = df["Calories"].var()
print("variance value: ", x)
x = df["Calories"].sum()
print("sum value: ", x)
x = df["Calories"].min()
print("minimum value: ", x)
x = df["Calories"].max()
print("maximum value: ", x)

#--------------------------------------------
#Cleaning Data of Wrong Format
df["Date"] = pd.to_datetime(df["Date"]) # convert the data type of the "Date" column to datetime
print(df.to_string())

#--------------------------------------------
#Replacing Values
df.loc[0, 'Duration'] = 12 # replace the value of the 7th row and the "Duration" column with 45
print(df.to_string())

for x in df.index:
  if df.loc[x, "Duration"] > 45:
    df.loc[x, "Duration"] = 45
# replace the values of the "Duration" column that are greater than 45 with 45
print(df.to_string())

#--------------------------------------------
#Removing duplicates data
print(df.duplicated()) # check for duplicates
# Add a duplicate row
df.loc[6] = df.loc[3]
print(df.duplicated()) # check for duplicates
df.drop_duplicates(inplace=True) # remove duplicates
print(df.to_string())