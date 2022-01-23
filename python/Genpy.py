# https://www.codewars.com/kata/51b66044bce5799a7f000003
'''
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below.
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left
most digit and skipping any digit with a value of zero. In Roman numerals 1990 is
rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
'''


class RomanNumerals:

    def to_roman(val):
        RomanNumerals.symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, 1000: "M", 500: "D",
                                 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        len(list(str(val)))
        x = []
        y = []
        z = []
        for index, i in enumerate(list(str(val))):
            # 10**(len(str(val))-index-1) - place value
            x.append(10 ** (len(str(val)) - index - 1))
            y.append(int(i))
        # break it into
        for i, j in zip(y, x):
            # i unit, j decimal place

            if i == 4 or i == 9 or i == 0:
                if i == 4:
                    z.append(f"{RomanNumerals.symbols[1 * j]}{RomanNumerals.symbols[5 * j]}")
                elif i == 9:
                    z.append(f"{RomanNumerals.symbols[1 * j]}{RomanNumerals.symbols[j * 10]}")
                else:
                    pass
            else:
                if i > 5:
                    z.append(f"{RomanNumerals.symbols[5 * j]}{RomanNumerals.symbols[j * 1] * (i - 5)}")
                else:
                    try:
                        z.append(f"{RomanNumerals.symbols[i * j]}")
                    except:
                        z.append(f"{RomanNumerals.symbols[j] * i}")
        return "".join(z)

    def from_roman(roman_num):
        val = 0
        for index, i in enumerate(roman_num):
            if index > 0:
                if RomanNumerals.symbols[i] <= RomanNumerals.symbols[roman_num[index - 1]]:
                    val += RomanNumerals.symbols[i]
                else:
                    val += RomanNumerals.symbols[i] - 2 * RomanNumerals.symbols[roman_num[index - 1]]
            else:
                val += RomanNumerals.symbols[i]
        return val