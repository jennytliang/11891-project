def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    roman_numeral = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_numeral += numeral
            number -= value

    return roman_numeral


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    """
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    roman_numeral = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_numeral += numeral
            number -= value

    return roman_numeral


def roman_to_int(roman_numeral):
    """
    Given a roman numeral, obtain its integer equivalent, and return it.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> roman_to_int('xix') == 19
    >>> roman_to_int('clii') == 152
    >>> roman_to_int('cdxxvi') == 426
    """
    roman_numerals = {
        'm': 1000,
        'cm': 900,
        'd': 500,
        'cd': 400,
        'c': 100,
        'xc': 90,
        'l': 50,
        'xl': 40,
        'x': 10,
        'ix': 9,
        'v': 5,
        'iv': 4,
        'i': 1
    }

    return sum(roman_numerals[numeral] for numeral in roman_numeral)
