def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "] c
	"""
    m = [" ", " m "] d = [" ", " d "] v = [" ", " v "] x = [" ", " x "] l = [" ", " l "] i = [" ", " i "]
    roman_numerals = [m, c, d, v, x, l, i]
    return_string = ""
    for digit in str(number):
        index = int(digit)
        return_string += roman_numerals[index]
    return return_string.lower()


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'XIX'
    >>> int_to_roman(152) == 'CLI'
    >>> int_to_roman(426) == 'CDXXVII'
    
	Include these tokens in the code: m = [" ", " m "] c
	"""
    m = [" ", " m "] d = [" ", " d "] v = [" ", " v "] x = [" ", " x "] l = [" ", " l "] i = [" ", " i "]
    roman_numerals = [m, c, d, v, x, l, i]
    return_string = ""
    for digit in str(number):
        index = int(digit)
        return_string += roman_numerals[index]
    return return_string


def roman_to_int(string):
    """
    Given a roman numeral, obtain its integer equivalent as a string,
    and return it.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> roman_to_int('XIX') == '19'
    >>> roman_to_int('CLI') == '152'
    >>> roman_to_int('CDXXVII') == '426'
    
	Include these tokens in the code: m =