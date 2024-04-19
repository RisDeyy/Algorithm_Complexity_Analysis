import numpy as np
import math
# Ham tinh he so trong 
# khai trien (x - 1)^n 
# su dung tam giac Pascal
# khai trien (x-1)^n se co n+1 he so
# tuong ung voi nCr * (-1)^(n-r)
# 0 <= r <= n
c = []
def coef(n):
    global c
    c = [0 for i in range(n+1)]
    c[0] = 1
    # i -> [0, n-1]
    for i in range(n):
        c[1+i] = 1
        # j -> [1,i]
        for j in range(i, 0, -1):
            c[j] = c[j-1] - c[j]
        c[0] = -c[0]
    return c

def isPrime(n):
    coef(n)
    i = math.floor(n /2) # he so doi xung
    c[0] += 1
    c[n] -= 1
    start = math.floor(n /2)
    end = 0
    while (i != 0 and (c[i] % n) == 0):
        i -= 1
    return i < 0

n = 4
coef(n)
print(c)
x = []
for i in range(math.floor(n /2), 0, -1):
    x.append(c[i])
print(x)