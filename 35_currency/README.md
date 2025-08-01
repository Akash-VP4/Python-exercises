Write a function named how_to_pay taking two parameters: amount and currency.

amount is an amount to pay.
currency describe the currency as a list of existing coins or banknotes.
The function should return a dict describing the easiest way to pay amount with the given currency.

For example, to pay 3 with a currency having coins of [1, 2, 5] you have to use one coin of 2 and one coin of 1, so the function should return {2: 1, 1: 1}.