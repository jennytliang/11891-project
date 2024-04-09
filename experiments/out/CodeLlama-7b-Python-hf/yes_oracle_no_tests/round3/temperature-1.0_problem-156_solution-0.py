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
    if number < 1 or number > 1000:
        print("Number is out of range")
        return

    m = [" ", " m "]
    str_number = str(number)

    if len(str_number) == 1:
        if number < 4:
            return m[0]
        elif number == 4:
            return "t"
        elif number < 9:
            return "ht"
        elif number == 9:
            return "ht"

    if len(str_number) == 2:
        if number < 40:
            return m[0] + int_to_mini_roman(int(str_number[1]))
        elif number == 40:
            return "x"
        elif number < 90:
            return "x" + int_to_mini_roman(int(str_number[1]))
        elif number == 90:
            return "x"

    if len(str_number) == 3:
        if number < 400:
            return int_to_mini_roman(int(str_number[2])) + int_to_mini_roman(int(str_number[1]))
        elif number == 400:
            return "c"
        elif number < 900:
            return "c" + int_to_mini_roman(int(str_number[2])) + int_to_mini_roman(int(str_number[1]))
        elif number == 900:
            return "c"


def mini_roman_to_int(string):
    """
    Given a roman numeral as a string, return its equivalent integer.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
