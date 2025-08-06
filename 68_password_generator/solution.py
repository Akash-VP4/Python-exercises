import random


def pwgen(length, with_digits=True, with_uppercase=True):

    pswd = ""

    for i in range(length):
        pswd += chr(random.randint(97, 122))
        # print(pswd)

    # print('Length:',length," pass: ",pswd)

    digits_posi = -1
    if with_digits:
        posi = random.randint(0, length - 1)
        pswd = pswd[:posi] + str(random.randint(0, 9)) + pswd[posi + 1 :]
        digits_posi = posi
        # print("after digits :",pswd)

    if with_uppercase:

        posi = random.randint(0, length - 1)
        pswd = pswd[:posi] + chr(random.randint(65, 90)) + pswd[posi + 1 :]

        # print("After uppercase: ",pswd)

        if digits_posi == posi:
            # print("recursion")
            return pwgen(length, with_digits, with_uppercase)

    return pswd

    # return pswd


# print("Final",pwgen(3))
