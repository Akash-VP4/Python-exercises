def fibonacci(num):
    sequence = [0, 1]
    for i in range(2, num):
        # print(i-2,i-1)
        # /sequence[i-1]
        sequence.append(sequence[i - 1] + sequence[i - 2])
        # sequence.append(i)
    return sequence
