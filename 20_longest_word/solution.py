def longest_word(text):
    text = text.replace("\n", " ")
    textArray = text.split(" ")

    longWord = textArray[0]

    for i in textArray:
        if len(longWord) < len(i):
            longWord = i

    return longWord
    ...
