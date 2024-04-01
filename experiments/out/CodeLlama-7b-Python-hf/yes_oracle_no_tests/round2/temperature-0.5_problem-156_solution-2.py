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
    
    m = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    
    roman = ""
    for a, b in zip(i, m):
        if a <= number:
            q, number = divmod(number, a)
            roman += q * b
    
    return roman.lower()


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = ["I", "IV", "V", "IX", "X", "L", "C", "D", "M"]
	"""
    
    m = ["I", "IV", "V", "IX", "X", "L", "C", "D", "M"]
    i = [1, 4, 5, 9, 10, 50, 100, 500, 1000]
    
    roman = ""
    for a, b in zip(i, m):
        if a <= number:
            q, number = divmod(number, a)
            roman += q * b
    
    return roman.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
