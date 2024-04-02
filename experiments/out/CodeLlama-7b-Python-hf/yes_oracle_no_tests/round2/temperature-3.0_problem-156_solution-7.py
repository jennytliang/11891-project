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
    m = ["I", "V", "X", "L", "C", "D", "M"]
    r = []
    for i in range(len(m) - 1, -1, -1):
        while number >= 5 * (10 ** i):
            r.append(m[i + 1])
            number -= 5 * (10 ** i)
        while number >= 1 * (10 ** i):
            r.append(m[i])
            number -= 1 * (10 ** i)
    return ''.join(r)


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "]
	"""
    m = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    r = []
    for i in range(len(m) - 1, -1, -1):
        while number >= 10 ** i:
            r.append(m[i])
            number -= 10 ** i
    return ''.join(r)


def roman_to_int(roman_str):
    """
    Given a roman numeral, convert it to an integer and return it.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> roman_to_int('xix') == 19
    >>> roman_to_int('clii') == 152
    >>> roman_to_int('cdxxvi') == 426
   