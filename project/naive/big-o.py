import math
import matplotlib.pyplot as plt
import numpy as np
import helper

count = 0

def naive(n):
    global count
    count += 1
    if (n % 2 == 0):
        return False
    for i in range(3, math.floor(math.sqrt(n)), 2):
        count += 1
        if (n % i == 0):
            return False
    return True

result = []
for i in range(2, 1000):
    count = 0
    naive(i)
    result.append(count)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

x = np.arange(2, 1000)
y = np.array(result)  # Assuming you have a valid 'result' array
axes[0].bar(x, y, label='Count')
y_sqrt = np.sqrt(x) * 0.5 
axes[0].plot(x, y_sqrt, color='red', label='Square Root of n')
axes[0].set_xlabel('n')
axes[0].set_ylabel('Count')


x = list(range(2, 1000))
y = []
for i in result:
    y.append(i**2)
axes[1].bar(x, y)
axes[1].set_xlabel('n')
axes[1].set_ylabel('count^2')
print(axes[1].get_ylim()[1])
print(type(axes[0]))
helper.plot_diagonal(axes[1], 'red')

plt.show()