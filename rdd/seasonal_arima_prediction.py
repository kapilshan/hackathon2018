import pandas as pd 
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt 
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from sklearn.metrics import mean_squared_error
from math import sqrt

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
fit1 = sm.tsa.statespace.SARIMAX(train.Revenue,order=(2, 0, 2),seasonal_order=(0,1,1,1),enforce_stationarity=False,
enforce_invertibility=False).fit()
y_hat_avg['SARIMA'] = fit1.predict(start="2015-01", end="2017-12", dynamic=True)
plt.figure(figsize=(16,8))
plt.plot( train['Revenue'], label='Train')
plt.plot(test['Revenue'], label='Test')
plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(test.Revenue, y_hat_avg.SARIMA))
print('Root Mean Square: %s' % rms) # RMSE: 100583.928043
