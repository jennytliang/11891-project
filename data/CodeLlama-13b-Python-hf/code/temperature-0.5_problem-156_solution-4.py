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
    if number < 1 or number > 1000:
        raise ValueError('number must be between 1 and 1000')

    roman_numerals = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i'),
    ]

    result = ''
    for numeral, roman in roman_numerals:
        while number >= numeral:
            result += roman
            number -= numeral

    return result.lower()


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 3999

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    >>> int_to_roman(3999) == 'mmmcmxix'
    """
    if number < 1 or number > 3999:
        raise ValueError('number must be between 1 and 3999')

    roman_numerals = [
        (1000, 'm'),
        (900, 'cm'),
        (500, 'd'),
        (400, 'cd'),
        (100, 'c'),
        (90, 'xc'),
        (50, 'l'),
        (40, 'xl'),
        (10, 'x'),
        (9, 'ix'),
        (5, 'v'),
        (4, 'iv'),
        (1, 'i'),
    ]

    result = ''
    for numeral, roman in roman_numerals:
        while number >= numeral:
            result += roman
            number -= numeral

    return result.lower()
