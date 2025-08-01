import math


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


num = 100_000_000

while not is_prime(num):
    num += 1

print(num)
