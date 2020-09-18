
import math
import random

#определение длины циклов в тесте миллера и запуск k-раундов
def isPrime(n):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    k = int(math.log2(n))
    t = n - 1
    while t % 2 == 0:
        t //= 2
    for i in range(k):
        if not miller_test(n, t):
            return False
    return True

#алгоритм теста миллера-рабина на простоту
def miller_test(n, t):
    from model import fast_power
    a = 2 + random.randint(1, n - 4)
    x = fast_power(a, t, n)
    if x == 1 or x == n - 1:
        return True
    while t != n - 1:
        x = (x ** 2) % n
        t *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

if __name__ == "__main__":
    for i in range(10 ** 26, 10 ** 27):
        if isPrime(i):
            print("Простое число:", i)
