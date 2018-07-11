import matplotlib.pyplot as plt
import numpy as np

# import data with loadtxt, but only the relevant floats. 
# data.csv is the file as you have given it above
data = np.loadtxt('CreditCardAuthorization.csv', delimiter=',', skiprows = 1, usecols = range(1,4))
data = data.transpose()

# import the tick labels
xt = np.loadtxt('CreditCardAuthorization.csv', dtype='str', delimiter=',', skiprows = 1, usecols = (0,))
width = 0.45
ind = np.arange(len(data[0])) + 0.75

fig, ax = plt.subplots(1,1)
p0 = ax.bar(ind, data[0], width, color = 'cyan')
p1 = ax.bar(ind, data[1], width, bottom = data[0], color = 'violet')
p2 = ax.bar(ind, data[2], width, bottom = data[0] + data[1], color = 'g')
#p3 = ax.bar(ind, data[3], width, bottom = data[0] + data[1] + data[2], color = 'r')

ax.set_ylabel('Amount')
ax.set_xlabel('Year')
ax.set_xticks (ind + width/2.)
ax.set_xticklabels( xt, rotation = 70 )

fig.suptitle('CreditCard Authorization', fontsize=15 )
fig.legend( (p0[0], p1[0], p2[0]), ('Revenue', 'Merchants_Live', 'Merchants_Trial') )
fig.tight_layout()
plt.show()
