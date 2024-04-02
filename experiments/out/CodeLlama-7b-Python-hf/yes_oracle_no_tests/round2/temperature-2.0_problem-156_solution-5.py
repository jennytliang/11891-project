def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: ",
	"""

    mr = ''
    if number > 1000:
        raise ValueError('Number too large')
    if number < 1:
        raise ValueError('Number too small')

    if number >= 1000:
        mr += 'm' * (number // 1000)
        number = number % 1000
    if number >= 500:
        mr += 'd' * (number // 500)
        number = number % 500
    if number >= 100:
        mr += 'c' * (number // 100)
        number = number % 100
    if number >= 50:
        mr += 'l' * (number // 50)
        number = number % 50
    if number >= 10:
        mr += 'x' * (number // 10)
        number = number % 10
    if number >= 5:
        mr += 'v' * (number // 5)
        number = number % 5
    if number >= 1:
        mr += 'i' * (number // 1)
        number = number % 1
    return mr


def mini_roman_to_int(roman_string):
    """
    Given a roman numeral as a string, convert it to an integer and return it.
    Restrictions:
    - roman_string is all lowercase.
    - roman_string is a valid roman numeral.
    - 1 <= len(roman_string) <= 16

    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426

    """

    if len(roman_string) > 16:
        raise ValueError('String too long')
    if len(roman_string) < 1:
        raise ValueError('String too short')