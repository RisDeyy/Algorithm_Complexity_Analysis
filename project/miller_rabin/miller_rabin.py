import math

# O(log(e)) ma e = log(n-1) -> log(n) 
def binpower(base, e, mod):
    result = 1
    base %= mod
    # O(log(e)), e /= 2 sau moi lan lap
    while (e):
        if (e & 1): # e % 2 != 0
            result = result * base % mod
        base = base * base % mod
        e >>= 1
    return result

print(binpower(2,4,5)) # 2^4 % 5 = 1
print(binpower(3,2,5)) # 3^2 % 5 = 4

# kiem tra a**d % n == 1 hoac a**(2**r * d) % n == n - 1
# O(logn)
def check_composite(n,a,d,s):
    # O(log(n)) (dong 3)
    x = binpower(a,d,n)
    # 1 hoac 2 gan
    if (x == 1 or x == n - 1):
        return False
    # O(s) ma s = log(n-1) (dong 40) -> O(log(n)) 
    for r in range(1,s): # 0 <= r <= s - 1
        x = x ** 2 % n # 2 gan
        if (x == n - 1): # 1 gan, 1 so sanh
            return False
    return True
# O(klog(n))
def MillerRabin(n, iter = 5):
    if (n < 4):
        return n == 2 and n == 3
    
    # 2 gan
    s = 0
    d = n - 1
    # tinh s = log(n-1)
    while ((d & 1) == 0): # d % 2 == 0
        d >>= 1
        s += 1
    # O(klog(n)), k = iter
    for i in range(iter):
        a = 2 + math.rand() % (n - 3) # [2, n-2]
        if (check_composite(n,a,d,s)): # O(log(n)) (dong 19)
            return False
        
    return True