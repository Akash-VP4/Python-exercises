import math


def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


for val in range(222281, 222381):
    binaryVal = bin(val)[2:]  # to avoid 0b

    sumBin = 0
    for digit in binaryVal:
        sumBin += int(digit)
    if is_prime(sumBin):
        print(val)
