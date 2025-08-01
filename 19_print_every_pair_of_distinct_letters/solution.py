from string import ascii_lowercase

letters = ascii_lowercase

for letter1 in letters:
    for letter2 in letters:
        if letter1 != letter2:
            print(letter1 + letter2)
