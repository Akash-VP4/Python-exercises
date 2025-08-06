def filtered(items, func):
    first = True
    res = []
    for i in items:
        if func(i):
            res.append(i)
            if first:
                print(i, end="")
                first = False
            else:

                print(",", i, end="")
    print("")

    return res


mult_of3 = filtered([i for i in range(101)], lambda x: x % 3 == 0)
mult_of5 = filtered([i for i in range(101)], lambda x: x % 5 == 0)
mult_of15 = filtered([i for i in range(101)], lambda x: x % 15 == 0)
