import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt('data.csv', delimiter=',', skip_header=10, skip_footer=10, names=['x', 'y', 'z'])
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.plot(data['x'], data['y'], color='r', label='the data')


