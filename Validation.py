#Find and remove missing data

import numpy as np
import pandas as pd

#Check if the data frames contains NA
print(df.isnull())
#Drop NA values
print(df.dropna())
#Drop columns where cells have NAs
print(df.dropna(axis=1))
#Drop columns where ALL cells have NAs
print(df.dropna(axis=1,how="all"))
#thresh parameter lets you specify a minimum number of non-null values for the row/column to be kept
print(df.dropna(thresh=2))
#Fill NA entries with zero
print(df.fillna(0))
#Specify a forward-fill to propagate the previous value forward
print(df.fillna(method="ffill"))
#Fill forward column wise
print(df.fillna(method="ffill",axis=1))
#Back-fill to propagate the next values backward
print(df.fillna(method="bfill"))

#Conditional Selction
#Isolate a column
data['Countries']
#Isolate rows
data[3:10]
#Isolate the portion of df containing languages with less than 5000 speakers
data[data['Number of speakers']<5000] 
#remove the first row, row at index 0
df.drop(df.index[0], inplace=True) 
#remove the first 2 rows
df.drop(df.index[:2], inplace=True)  
#drop column called latitude
df.drop(['Latitude'], axis = 1, inplace = True) 