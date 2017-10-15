#INPUT from txt, Excel, JSON, and HTML

#Read in a very simple CSV file
file="F:\\Python_ML\\Course6_Python4DS\\scriptsLecture\\section4\\Resp2.csv"
df1=pd.read_csv(file)
df1.head()

#Read in CSV when the seperator is ;
file="F:\\Python_ML\\Course6_Python4DS\\scriptsLecture\\section4\\winequality-red.csv"
df1=pd.read_csv(file)
df1=pd.read_csv(file, sep = ";")
df1.head()

#Read in .txt file
df1=pd.read_csv("bostonTxt.txt") 
#tab seperated
df1=pd.read_csv("bostonTxt.txt", sep = "\t")
df1.head()

#Read in Excel
file="F:\\Python_ML\\Course6_Python4DS\\scriptsLecture\\section4\\boston1.xls"

# Load spreadsheet
xl = pd.ExcelFile(file)
# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Sheet1')

#Read in JSON
import pandas as pd
import json

df = pd.read_json("skorea.json")
web = pd.read_json('https://api.github.com/repos/pydata/pandas/issues?per_page=5')

#Read in HTML
import pandas as pd
import html5lib

uss=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states') 
print(type(uss)) # #this is a list of dataframes

u = uss[0] #grab dataframe from index 0
print(type(u))

url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url) #this is a list of dataframes
print(type(dfs))

df = dfs[0] #list of dataframes

whsSK=pd.read_html('https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_South_Korea') 
whs_sk = whsSK[0] #grab dataframe from index 0
print(whs_sk)

#page with 1+ table
whsPH=pd.read_html('https://en.wikipedia.org/wiki/List_of_World_Heritage_Sites_in_the_Philippines') 
whs_phl = whsPH[2] #grab dataframe from index 1, table 2 of the tentative WHS sites
print(whs_phl)