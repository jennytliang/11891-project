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
    roman_numerals = {1: 'i', 2: 'x', 3: 'c', 4: 'd', 5: 'v', 6: 'l', 7: 'i'}
    roman_numerals_10 = {10: 'x', 20: 'l', 30: 'c', 40: 'd', 50: 'v', 60: 'i'}
    num_string = str(number)
    num_list = list(num_string)
    num_list.reverse()
    mini_roman = ''
    for i in num_list:
        if int(i) > 5:
            mini_roman += roman_numerals[int(i)] + roman_numerals_10[10 * int(i)]
        elif int(i) == 5:
            mini_roman += roman_numerals[10 * int(i)]
        else:
            mini_roman += roman_numerals[int(i)]
    return mini_roman.lower()


def mini_roman_to_int(roman_numeral):
    """
    Given a roman numeral, return its corresponding positive integer.
    Restrictions:
    - 1 <= numeral <= 1000
    - numeral is in lowercase
    - numeral is in roman format
    
    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
    
	Include these tokens in the code: m = [" ", " m "]
    """
    m = [" ", " m "]
    roman_numerals = {1: 'i', 2: 'x', 3: 'c', 4: 'd', 5: 'v', 6: 'l', 7: 'i'}
    roman_numerals_10 = {10: 'x', 