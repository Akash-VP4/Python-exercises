def from_roman_numeral(roman_numeral):

    val = 0
    rom_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev = rom_int.get(roman_numeral[0])

    for i in range(len(roman_numeral)):

        crnt = rom_int.get(roman_numeral[i])

        if prev < crnt:
            val -= prev * 2

        val += crnt
        prev = crnt

        # print(val)

    return val
