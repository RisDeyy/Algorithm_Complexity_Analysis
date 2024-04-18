import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# for k in range(1,9):
#     exponent = k
#     total_count = 0
#     thousandths = 10 ** exponent / 100
#     progress = 0 
#     n = 10 ** exponent
#     for i in range(2, n):
#         count = 0
#         naive(i)
#         total_count += count
#     average = total_count / (n-2)
#     print(average)

data = pd.read_csv('average-case.csv')
print(data)
x = data['log10']
y = data['average-count']
axes[0].bar(x, y)
axes[0].set_xlabel('log10(n)')
axes[0].set_ylabel('average-count')
y_exponent = []
for i in x:
    y_exponent.append(2**i) 
axes[0].plot(x, y_exponent, color='red')

y = np.log2(data['average-count'])
axes[1].bar(x, y)
axes[1].set_xlabel('log10(n)')
axes[1].set_ylabel('log(average-count)')
helper.plot_diagonal(axes[1], color='red')

plt.show()