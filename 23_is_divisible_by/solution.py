def findDigitSum(num):
    digitSum = 0

    while num > 0:
        digitSum += num % 10
        num //= 10

    return digitSum


for num in range(1001):
    if num % 7 == 0:
        if findDigitSum(num) % 3 == 0:
            print(num)
