import random
import math
import time
import numpy as np


# алгоритм возведения в степень по модулю

def fast_power(a, b, n):
    return pow(a, b, n)
    # функция не выгодная по времени работы, заменяем на стандартную
    """if n == 1 and a != 0:
        return 0
    if a == 0:
        return 0
    if b == 0:
        return 1
    a = a % n
    res = 1
    while (b > 0):
        if ((b & 1) == 1):
            res = (res * a) % n
        b = b >> 1
        a = (a * a) % n
    return res"""


def switch_num(i):
    switcher = {0: range(0, 2 ** 7),
                1: range(2 ** 7 + 1, 2 ** 12, 2),
                2: range(2 ** 12 + 1, 2 ** 17, 2),
                3: range(2 ** 17 + 1, 2 ** 20, 2),
                4: range(2 ** 20 + 1, 2 ** 22, 2),
                5: range(2 ** 22 + 1, 2 ** 24, 2),
                6: range(2 ** 24 + 1, 2 ** 26, 2)}
    return switcher.get(i)


def switch_test(i, n):
    from fermat import fermat
    from lehmann import lehmann
    from miller_rabin import isPrime
    from solovey_strassen import solovoyStrassen
    switcher = {0: lambda: fermat(n),
                1: lambda: lehmann(n),
                2: lambda: solovoyStrassen(n),
                3: lambda: isPrime(n)}
    return switcher.get(i, lambda: None)()
