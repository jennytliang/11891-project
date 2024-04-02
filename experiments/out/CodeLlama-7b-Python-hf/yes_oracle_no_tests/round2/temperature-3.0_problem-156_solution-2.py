def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: # Your code here
	"""
    if number == 1000:
        return 'm'

    if number < 1000:
        if number >= 500:
            return 'd' + int_to_mini_roman(number-500)
        if number >= 100:
            return 'c' + int_to_mini_roman(number-100)
        if number >= 50:
            return 'l' + int_to_mini_roman(number-50)
        if number >= 10:
            return 'x' + int_to_mini_roman(number-10)
        if number >= 5:
            return 'v' + int_to_mini_roman(number-5)
        if number >= 1:
            return 'i' + int_to_mini_roman(number-1)
    return ''


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: # Your code here
	"""
    if number == 1000:
        return 'm'

    if number < 1000:
        if number >= 500:
            return 'd' + int_to_roman(number-500)
        if number >= 100:
            return 'c' + int_to_roman(number-100)
        if number >= 50:
            return 'l' + int_to_roman(number-50)
        if number >= 10:
            return 'x' + int_to_roman(