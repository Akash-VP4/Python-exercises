from string import ascii_lowercase

alpha = list(ascii_lowercase)


def caesar_cypher_encrypt(s, key):

    encripted = ""

    for letter in s:
        if not letter.isalpha():
            encripted += letter
            continue
        posi = alpha.index(letter.lower())
        encript_Posi = (key + posi) % 26

        if letter.isupper():
            encripted += alpha[encript_Posi].upper()

        else:
            encripted += alpha[encript_Posi]

    # print("encripted: ",encripted)
    return encripted


def caesar_cypher_decrypt(s, key):

    decripted = ""

    for letter in s:
        if not letter.isalpha():
            decripted += letter
            continue
        posi = alpha.index(letter.lower())
        decript_posi = (key) % 26
        if decript_posi < 0:
            decript_posi = 26 + decript_posi

        decript_posi = posi - decript_posi

        if letter.isupper():
            decripted += alpha[decript_posi].upper()

        else:
            decripted += alpha[decript_posi]

    # print("encripted: ",decripted)
    return decripted
