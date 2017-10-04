	#DS Templates

	#Import packages as required
	import numpy as np                #Supports large arrays and matricies
	import pandas as pd               #Provides table headers and column numbers
	import matplotlib.pyplot as plt   #Basic graphics package
	import seaborn as sbn             #Advanced graphics package
	import os                         #To work with the file system
	import warnings
	warnings.filterwarnings('ignore') #Supress warnings, may be needed in some instances

	print(os.getcwd())   #Print working directory
	os.chdir('C:\\PATH\\') #Change working directory
	
	#Import dataset and headers with pandas
	dataset = pd.read.csv('C:\\PATH\\')
	
	#Explore Data
	len(df)       #Gets number of rows
	df.columns()  #Column names
	df.head(#)    #First # of defined rows
	df.tail(#)    #Last # of defined rows
	df.info()     #Dataset structure
	df.describe() #Summary statistics
	
	#Subset dataset by row
	newdf = df[#:#] Slice by range
	#Subset dataset by column
	colList = ['columns', 'to', 'be', 'subsetted']
	newdf = [[colList]]
	#Subset column and row
	newdf = [#:#][[colList]]
	#Convert column to catagorical type
	df.colName = df.colName.astype('catagory')
	
	#Working with matricies. Assumes column and row will be consistent throughout
	#Create a ColumnName list and index dictionary
	colName = ['ColumnName', '...']
	hdict = {'ColumnName':0, '...':1}
	#Create list of row values
	row1 = [values, values, ...]
	row2 = [values, values, ...]
	#Create a matrix from row values
	matrixName = np.array([row1, row2, ....])
	#Matrix can be searched across matricies:
	newMatrix = [hDict['colName'], pDict['row']]
	
	#Derived/calculated column
	df['newCol'] = df.column */-+ df.column
	#Remove column
	df.drop('colName')
	
	#Filters, multiple must use bitwise logical operator & | to work within tables
	filter1 = fc.column ><== #
	filter2 = (fc.column < #) & (fc.column < #)
	fdf = df[filter1]
	
	#Access singular cells within dataset
	df.at[#,'colName'] Finds cell by the label
	df.iat[#,#]        Finds cell based on count
	
	#Create a chart to plot a column by a catagorical variable, check Seaborn Gallery for examples
	list1 = list() #Empty list
	myLabels = list() #For chart 
	for i in #dataset catagory:
		list1.append(#dataset[dataset.catagory == i].column)
		labels.append(i)
	h = plt.#Chart type(list1, parameters for specific chart, label = myLabels)
	plt.legend()
	plt.show
	
	