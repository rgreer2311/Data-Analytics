#Pandas
import numpy as np
import pandas as pd

#pandas Series: one-dimensional array with labels
#obtain series from Python dictionaries (data structure for storing key-value pairs)
#keys of dictionaries act as index or label for values
dict={'a' : 3, 'b' : 'cat', 'c' : 2.5}
pd.Series(dict)

#List to series
oneD = pd.Series([100, 'cat', 310, 'gog', 500], ['Amy', 'Bobby', 'Cat', 'Don', 'Emma'])
#the second list contains index, index is the label of values
oneD = pd.Series([100, 'cat', 310, 'gog', 500], index=['Amy', 'Bobby', 'Cat', 'Don', 'Emma']) 
#loc is a label-location based indexer for selection by labels- Cat and Donna
oneD.loc[['Cat','Emma']] 
#extract the data at index 0, 3 and 4
oneD[[0,3,4]] 
#.iloc is primarily integer position based (from 0 to length-1 of the axis). access index 1
oneD.iloc[1] 

#DataFrames- 2D data structure. Stores data in tabular form (rows and columns)
d = {'A' : pd.Series([100., 200., 300.], index=['apple', 'pear', 'orange']),
     'B' : pd.Series([111., 222., 333., 4444.], index=['apple', 'pear', 'orange', 'melon'])}
	 df = pd.DataFrame(d)
#list index values
df.index 
#column names
df.columns 
#specify which row/index and column we want to retain
pd.DataFrame(df, index=['orange', 'melon', 'apple'], columns=['A']) 

























