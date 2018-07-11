import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
#Importing data
#df = pd.read_csv('CreditCardAuthorization.csv')
#Printing head
#df.head()
#Printing tail
#df.tail()

#Subsetting the dataset
#Index 11856 marks the end of year 2013
df = pd.read_csv('CreditCardAuthorization.csv', nrows = 37)

#Creating train and test set 
#Index 10392 marks the end of October 2013 
train=df[0:25] 
test=df[26:]

#Aggregating the dataset at daily level
df.Timestamp = pd.to_datetime(df.Year,format='%Y-%m') 
df.index = df.Timestamp 
#df = df.resample('D').mean()
train.Timestamp = pd.to_datetime(train.Year,format='%Y-%m') 
train.index = train.Timestamp 
#train = train.resample('D').mean() 
test.Timestamp = pd.to_datetime(test.Year,format='%Y-%m') 
test.index = test.Timestamp 
#test = test.resample('D').mean()

#Plotting data
train.Revenue.plot(figsize=(15,8), title= 'Monthly Revenue', fontsize=14)
train.Merchants_LIVE.plot(figsize=(15,8), title= 'Monthly Live', fontsize=14)
train.Merchants_TEST.plot(figsize=(15,8), title= 'Monthly Test', fontsize=14)
test.Revenue.plot(figsize=(15,8), title= 'Monthly Revenue', fontsize=14)
test.Merchants_LIVE.plot(figsize=(15,8), title= 'Monthly Live', fontsize=14)
test.Merchants_TEST.plot(figsize=(15,8), title= 'Monthly Data', fontsize=14)
plt.show()
