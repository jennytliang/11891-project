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
    roman_numerals = [
        "i", "x", "c", "m", "v", "l", "d"
    ]
    # Your code here
    result = ''
    while number > 0:
        for i in range(len(m)):
            if number - 10 ** i >= 0:
                result += roman_numerals[i]
                number -= 10 ** i
                break
    return result


def int_to_mini_roman2(number):
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
    roman_numerals = [
        "i", "x", "c", "m", "v", "l", "d"
    ]
    # Your code here
    result = ''
    while number > 0:
        for i in range(len(m)):
            if number - 10 ** i >= 0:
                result += roman_numerals[i]
                number -= 10 ** i
                break
    return result


def int_to_mini_roman3(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>>