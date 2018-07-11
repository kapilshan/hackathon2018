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

y_hat_avg = test.copy()
y_hat_avg['avg_forecast'] = train['Revenue'].mean()

from sklearn.metrics import mean_squared_error
from math import sqrt
rms = sqrt(mean_squared_error(test.Revenue, y_hat_avg.avg_forecast))
print('Root Mean Square: %s' % rms) #RMSE = 21865.7166598

plt.figure(figsize=(12,8))
plt.plot(train['Revenue'], label='Train')
plt.plot(test['Revenue'], label='Test')
plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
plt.legend(loc='best')
plt.title("Avearge Forecast")
plt.show()
