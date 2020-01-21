import numpy as np
import pandas as pd
import html5lib

import os

os.getcwd()
os.chdir('C:\\Users\\uC260543\\Work\\PythonPractices\\DataSciencePy\\scriptsLecture\\scriptsLecture\\section5\\')
### S5: DATA WRANGLING / MANIPULATION


##S5.2 - 5.3 Basic Data Handling: Starting with Conditional Data Selection
file = 'C:\\Users\\uC260543\\Work\\PythonPractices\\DataSciencePy\\scriptsLecture\\scriptsLecture\\section5\\endangeredLang.csv'
data = pd.read_csv('endangeredLang.csv')
data.head(n=6)

#isolate a column
data['Countries']

#isolate 2 columns
df=data[['Countries','Name in English']]

df.head(6)

#isolates rows
data[3:10] ##only print from 3 to 9

#data conditional selection
data[data['Number of speakers']<5000] #isolate the portion of


### S4: READ CSV, EXCEL, HTML AND JSON DATA TO PYTHON USING PANDA

## Read in HTML file
import pandas as pd
import html5lib
import BeautifulSoup4 as bs4
url = 'https://simple.wikipedia.org/wiki/List_of_U.S._states'
uss = pd.read_html(url, flavor='bs4')
print(type(uss))
print(uss)

u = uss[0] ## collect the 1st table of the website 
print(u)

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url) #list of dataframes
print(type(dfs))

df = dfs[0]
df
##Read in xls file
#Load spreadsheet
file = "C:\\Users\\uC260543\\Work\\PythonPractices\\DataSciencePy\\scriptsLecture\\scriptsLecture\\section4\\boston1.xls"
xl = pd.ExcelFile(file)
print(xl.sheet_names)
#load a sheet into dataframe
df1 = xl.parse('Sheet1')
df1.head(10)


##Read in csv file
file = "C:\\Users\\uC260543\\Work\\PythonPractices\\DataSciencePy\\scriptsLecture\\scriptsLecture\\section4\\resp2.csv"
df1 = pd.read_csv(file)
df1.head(7) ##show the first 7 rows

## unstructured csv file with seperation
file = "C:\\Users\\uC260543\\Work\\PythonPractices\\DataSciencePy\\scriptsLecture\\scriptsLecture\\section4\\winequality-red.csv"
df2 = pd.read_csv(file, sep=";")
df2.head(7) ##show the first 7 rows



#pandas series 
dict = {'a' : 3, 'b' : 'cat', 'c' : 2.5}
pd.Series(dict) #

oneD = pd.Series([100,'cat',310,'gog',500],
            index=['Amy','Bobby','Cat', 'Don', 'Emma'])
oneD

oneD.loc[['Cat','Emma']] #Loc is a label-location based index for selection by lables
oneD.iloc[1] # .iloc is primarliy integer location

'cat' in oneD # check if 'cat' is in the series indexes --> false
'Cat' in oneD #--> true

d = {
    'A': pd.Series([100.,200.,300.], index=['apple','pear', 'orange']),
    'B' : pd.Series([111., 222., 333., 4444.], index=['apple', 'pear', 'orange', 'melon'])
}

df = pd.DataFrame(d)
df
print(type(df))

df.index #list index values
df.columns # column names
#Subsetting: specify whic row/index and colmn we want to retain
pd.DataFrame(df,index=['orange', 'melon', 'apple'], columns=['A'])


#Data frames - 2D data structure. stoers data in tabular form
#<class 'pandas.core.frame.DataFrame'

### S3:8 NUMPY STATISTIC

arr =[[1,2,3,4],[3,4,5,6],[7,8,9,10],[12,7,10,9],[2,11,8,19]] 
narr = np.array(arr)
print(narr)

narr.sum() # sum al values of array
narr.sum(axis=0) # column wisesum
narr.sum(axis=1) # row wise sum
narr.mean(axis=0) # columns mean
#median, variance and pcntile
np.median(narr,axis=1)
np.std(narr,axis=1)
np.percentile(narr,50,axis=1) #50th percentile of each row

### S3:5 - 6 NUMPY FOR BASIC VECTOR AND MATRIX ARITHMETIC 
x= np.array([1,2,3])
y= np.array([[2,3,4],[3,6,8]])
z = np.transpose(y)
print(x)
print(y)
print(z)
print(x+y)
print(x + 2) #addition with a scalar
print(x*y) #hadmard product
print(np.dot(y,x)) # dot product
print(y/x)


### S3:3 NUMPY OPERATIONS ## Rank1 array

a = [1,2,11,6,8,18,2]
na = np.array(a)
print(na)
print(np.shape(na)) #its a rank 1 numpy array with 7 items

#lets print out from start to index 3 element
print(na[:3])

# use a step of 2:
print(na[1:5:2]) # [2 6]

#last item
print(na[-1])

#reverse order
print(na[-7:-3])
#copy an array: 
b = na[:]
print(b)

# concatenate 2 arrays
x = np.array([2,6,8,4])
y = np.array([11,8,2])
z = np.concatenate([x,y])
print(z)

#MULTIDIMENSION ARRAY OPERATIONS
arr=[[1,2,3,4],[3,4,5,6],[7,8,9,6],[12,7,10,9],[2,11,8,10]]
narr = np.array(arr)
print(narr)

#print the first row
print(narr[0])
print(narr[1,0]) #print the element at 2nd row, 1 column
narr[3,0] = 14 # replace content
print(narr)

#get the last row
print(narr[-1]) 

# print row an column
print(narr)
print(narr[1:4,2:5]) #row 1-4 and col 2-5 

# concatenate row and col wise
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
c = np.concatenate((a,b))
d = np.concatenate((b,a,a))
print(d)
print(c)