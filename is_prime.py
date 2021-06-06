"""
Input
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

Prime number
[2, 3, 5, 7, 11, 13, 17, 19]

Non prime number
[1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

"""
import math


def is_prime_v1(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def is_prime_v2(num):
    if num <= 1:
        return False
    
    # for i in range(2, math.floor(math.sqrt(num) + 1)):
    #     if num % i == 0:
    #         return False

    i = 2
    while i * i == 0:
        if num % i == 0:
            return False
        i += 1

    return True        


def is_prime_v3(num):
    if num <= 1:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False

    i = 3
    while i * i == 0:
        if num % i == 0:
            return False
        i += 2

    return True    

if __name__ == '__main__':
    import time
    import random

    numbers = [random.randint(0, 1000) for _ in range(100000)]

    start = time.time()
    for num in numbers:
        is_prime_v1(num)
    print('v1', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print('v2', time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print('v3', time.time() - start)