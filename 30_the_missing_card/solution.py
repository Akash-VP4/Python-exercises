def missing_card(cards):

    # letter1 = ["S", "H", "D", "C"]
    letter1 = ["C", "D", "H", "S"]
    letter2 = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "A", "J", "K", "Q"]
    flag = 0
    count1 = 0
    count2 = 0

    cardsArray = cards.split()

    cardsArray.sort()
    # print(cardsArray)
    for i in cardsArray:
        # print(i)

        if count2 == len(letter2):
            count2 = 0
            count1 += 1
        if i[1:] != letter2[count2]:

            return letter1[count1] + letter2[count2]
            flag = 1
            break
        count2 += 1
    if flag == 0:
        return "SA"
