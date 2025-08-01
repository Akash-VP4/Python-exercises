def how_to_pay(amount, currency):
    currency.sort()

    dict = {}

    i = len(currency) - 1

    while i >= 0 and amount > 0:

        currentCurrency = currency[i]
        # print(currentCurrency)

        if amount >= currentCurrency:
            # print(amount," ",currentCurrency," ",amount//currentCurrency)
            dict[currentCurrency] = amount // currentCurrency
            amount %= currentCurrency

        i -= 1

    return dict
