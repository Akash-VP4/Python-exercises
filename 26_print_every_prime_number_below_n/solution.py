import math

firstPrime = True

for i in range(10000, 10050):
    isprime = True
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        if firstPrime:
            print(i, end="")
            firstPrime = False

        print(",", i, end="")
