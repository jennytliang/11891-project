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
    to_roman = {1000: "m", 900: "cm", 500: "d", 400: "cd", 100: "c", 90: "xc", 50: "l", 40: "xl", 10: "x", 9: "ix", 5: "v", 4: "iv", 1: "i"}
    roman_numeral = ""
    for key in sorted(to_roman.keys(), reverse=True):
        while number >= key:
            roman_numeral += to_roman[key]
            number -= key
    return roman_numeral.lower()

def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string, and return it, in uppercase.
    Restrictions: 1 <= num <= 3000

    Examples:
    >>> int_to_roman(19) == 'XIX'
    >>> int_to_roman(152) == 'CLIV'
    >>> int_to_roman(426) == 'CDXXVI'
    
	Include these tokens in the code: m = [" ", " M "]
    """
    m = [" ", " M "]
    to_roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    roman_numeral = ""
    for key in sorted(to_roman.keys(), reverse=True):
        while number >= key:
            roman_numeral += to_roman[key]
            number -= key
    return roman_numeral.upper()

def roman_to_int(roman_numeral