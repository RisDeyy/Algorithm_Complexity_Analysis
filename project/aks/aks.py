import math
import threading
import time
import test
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import helper

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(k, n) == 1:
            amount += 1
    return amount

def step1(n):
    for b in range(2, math.floor(math.log2(n) + 1)):
        a = n ** (1 / b)
        if a.is_integer():
            return False
    return True

def step2(n):
    mk = math.floor(math.log2(n) ** 2)
    nexr = True
    r = 1
    while nexr:
        r += 1
        nexr = False
        k = 0
        while k <= mk and not nexr:
            k = k + 1
            if pow(n, k, r) in (0, 1):
                nexr = True
    return r

def step3(n, r):
    for a in range(1, r + 1):
        if 1 < math.gcd(a, n) < n:
            return False
    return True

def step4(n, r):
    if n <= r:
        # print(f"{n} - prime. Step 4")
        return True
    return False

def step5(n, r):
    max_val = math.sqrt(phi(r))
    rn = math.floor(max_val * math.log2(n))
    if rn > n:
        rn = n

    for a in range(0, rn):
        result = step5_check(n, a, a + 1)
        if not result:
            return False

    # If all checks passed, return True
    return True

def step5_concurrency(n, r):
    max = math.sqrt(phi(r))
    rn = math.floor(max * math.log2(n))
    if rn > n:
        rn = n
    threads = []
    ran = rn / 6 # my cpu has 6 cores
    ran = math.floor(ran)
    if ran == 0:
        ran = 1

    manager = threading.Manager()
    return_dict = manager.dict()

    for a in range(0, rn, ran):
        thread = threading.Thread(
            target=step5_check, args=(n, a, a + ran, return_dict)
        )
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()

    if False not in return_dict.values():
        # print(f"{n} - prime. Step 5")
        return True
    return False

def step5_check(n, bot, top, return_dict = None):
    x = bot / (top - bot)
    if bot == 0:
        bot = 1
    for a in range(bot, top):
        b = pow(a, n, n)
        if b - a != 0:
            if (return_dict is not None):
                return_dict[x] = False
            return False
    if (return_dict is not None):
        return_dict[x] = True
    return True

def aks(n):
    if step1(n):
        r = step2(n)
        return step3(n, r) and (step4(n, r) or step5(n, r))
    return False

def aks_concurrency(n):
    if step1(n):
        r = step2(n)
        return step3(n, r) and (step4(n, r) or step5_concurrency(n, r))
    return False

if __name__ == '__main__':
    # max_r = []
    # for k in range(20):
    #     n = 2**k
    #     result = []
    #     for i in range (2**(k-1)+1, 2**k):
    #         if test.isPrime(i):
    #             result.append(step2(i))
    #     max_r.append(max(result))
    # print(max_r)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 4))
    data = pd.read_csv('max_r.csv')
    print(data)
    x = data['log2']
    y = data['r']
    axes.bar(x, y)
    axes.set_xlim(6,22)
    axes.set_xlabel('log2(n)')
    axes.set_ylabel('r-value')
    axes.set_title('Giá tri step2(n)')
    helper.plot_diagonal(axes, 'red')

    plt.show()