def list_pretty_print(items):
    count = 0
    for i in range(len(items)):

        print(items[i], end="")

        count += 1
        if count == 5 or i == len(items) - 1:
            print("")
            count = 0
            # print("here")
        else:
            print(",", end="")
