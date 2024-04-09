def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    m = [" ", " m "]
    roman_numerals = {
        1: "i",
        2: "ii",
        3: "iii",
        4: "iv",
        5: "v",
        6: "vi",
        7: "vii",
        8: "viii",
        9: "ix",
        10: "x",
        11: "xi",
        12: "xii",
        13: "xiii",
        14: "xiv",
        15: "xv",
        16: "xvi",
        17: "xvii",
        18: "xviii",
        19: "xix",
        20: "xx",
        30: "xxx",
        40: "xl",
        50: "l",
        60: "lx",
        70: "lxx",
        80: "lxxi",
        90: "lxxx",
        100: "c",
        200: "cc",
        300: "ccc",
        400: "cd",
        500: "d",
        600: "dc",
        700: "dcc",
        800: "dcccx",
        900: "cm",
    }
    roman_number = ""
    for i in roman_numerals.keys():
        while number >= i:
            roman_number += roman_numerals[i]
            number -= i
    return roman_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
