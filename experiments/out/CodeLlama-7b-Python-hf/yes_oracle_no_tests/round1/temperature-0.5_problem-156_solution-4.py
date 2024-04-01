def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code:  m = [" ", "
	Do not include these tokens in the code: roman _ numer als { 1
	"""

    roman_numerals = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}
    roman_numeral_values = {1000: 1000, 900: 900, 500: 500, 400: 400, 100: 100, 90: 90, 50: 50, 40: 40, 10: 10, 9: 9, 5: 5, 4: 4, 1: 1}
    roman_numeral_string = ''
    current_number = number
    while current_number > 0:
        for key, value in roman_numeral_values.items():
            if current_number >= key:
                roman_numeral_string += roman_numerals[key]
                current_number -= key
    return roman_numeral_string

# def int_to_mini_roman(number):
#     """
#     Given a positive integer, obtain its roman numeral equivalent as a string,
#     and return it in lowercase.
#     Restrictions: 1 <= num <= 1000

#     Examples:
#     >>> int_to_mini_roman(19) == 'xix'
#     >>> int_to_mini_roman(152) == 'clii'
#     >>> int_to_mini_roman(426) == 'cdxxvi'
    
#     Include these tokens in the code:  m = [" ", "
#     Do not include these tokens in the code: roman _ numer als { 1
#     """

#     roman_numerals = {1000: 'm