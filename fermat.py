import numpy as np
import random
import math


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def fermat(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    k = int(math.log2(n))
    while k > 0:
        a = 2 + random.randint(1, n - 4)
        if np.gcd(n, a) != 1:
            return False
        from model import fast_power
        if fast_power(a, n - 1, n) != 1:
            return False
        k -= 1
    return True


if __name__ == "__main__":
    for i in range(10 ** 10 + 1, 10 ** 12, 2):
        if fermat(i):
            print("Простое число:", i)
