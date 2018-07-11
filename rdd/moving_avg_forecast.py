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
df.isnull().any()
df = df.fillna(lambda x: x.median())
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

y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['Revenue'].rolling(72013).mean().iloc[-1]
plt.figure(figsize=(16,8))
plt.plot(train['Revenue'], label='Train')
plt.plot(test['Revenue'], label='Test')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.show()
