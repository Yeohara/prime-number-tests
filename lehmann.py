import random
import math

def lehmann(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    k = int(math.log2(n))
    a = 2 + random.randint(1, n - 4)
    e = int((n - 1) / 2)

    while k > 0:
        from model import fast_power
        result = fast_power(a, e, n)
        if (result % n) == 1 or (result % n) == (n - 1):
            a = random.randint(2, n - 1)
            k -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    for i in range(1, 10**7):
        if lehmann(i):
            print("Простое число:", i)