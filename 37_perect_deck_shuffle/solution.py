def perfect_shuffle(deck):

    shuffled = []

    evenPosi = 0
    oddPosi = len(deck) // 2

    for i in range(len(deck)):
        if i % 2 == 0:
            shuffled.append(deck[evenPosi])
            evenPosi += 1
        else:
            shuffled.append(deck[oddPosi])
            oddPosi += 1

    return shuffled
    ...
