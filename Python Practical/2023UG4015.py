import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("AQI_Data.csv")

# Ques 1 :-

# a.) display the first 8 rows
print("the first 8 rows are - ")
print(data.head(8))

print("\n")

# b.) display the last 5 rows
print("the last 5 rows are - ")
print(data.tail(5))

print("\n")

# c.) show the dtype and number of non-null values in each column
print("the dtype and number of non-null values - ")
print(data.info())

print("\n")

# d.) use numpy to compute the mean AQI , max PM2.5 aand min PM10 values for each city
print("the mean AQI , max PM2.5 aand min PM10 values for each city - ")
print(data.groupby('City')['AQI'].mean())
print("\n")
print(data.groupby('City')['PM2.5'].max())
print("\n")
print(data.groupby('City')['PM10'].min())
print("\n")

print("\n")

# Ques 2 a.) Reanme the columns in the dataset such that:

# a.) "AQI" is renamed to "Air Quality Index"
data = data.rename(columns={'AQI': 'Air Quality Index'})

# b.) "PM2.5" is renamed to "Particular Matter 2.5"
data = data.rename(columns={'PM2.5': 'Particular Matter 2.5'}) 

# c.) "PM10" is renamed to "Particular Matter 10"
data = data.rename(columns={'PM10': 'Particular Matter 10'}) 

# d.) "City" is renamed to "Location"
data = data.rename(columns={'City': 'Location'})

# Ques 2 b.) Replace all occurences of the value "Unknown" in the City column with "Not Available"
data['Location'] = data['Location'].replace('Unknown', 'Not Available')


# display the updated dataset abd save it in a new file result.csv. If the file already exists, overwrite it; otherwise, create a new one
print("Updated dataset - ")
print(data)
data.to_csv('result.csv', index=False)
