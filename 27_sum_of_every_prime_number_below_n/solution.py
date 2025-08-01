import math


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def sum_primes(num):
    sum = 0
    for i in range(num):

        if is_prime(i):
            # print(i, is_prime(i))
            # print(num,i)
            sum += i
    return sum
