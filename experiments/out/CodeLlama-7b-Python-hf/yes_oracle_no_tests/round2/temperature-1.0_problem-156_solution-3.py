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

    mr_string = ""
    while number != 0:
        if number >= 1000:
            mr_string += "m"
            number -= 1000
        elif number >= 900:
            mr_string += "cm"
            number -= 900
        elif number >= 500:
            mr_string += "d"
            number -= 500
        elif number >= 400:
            mr_string += "cd"
            number -= 400
        elif number >= 100:
            mr_string += "c"
            number -= 100
        elif number >= 90:
            mr_string += "xc"
            number -= 90
        elif number >= 50:
            mr_string += "l"
            number -= 50
        elif number >= 40:
            mr_string += "xl"
            number -= 40
        elif number >= 10:
            mr_string += "x"
            number -= 10
        elif number >= 9:
            mr_string += "ix"
            number -= 9
        elif number >= 5:
            mr_string += "v"
            number -= 5
        elif number >= 4:
            mr_string += "iv"
            number -= 4
        elif number >= 1:
            mr_string += "i"
            number -= 1
    return mr_string

# print(int_to_mini_roman(19))
# print(int_to_mini_roman(152))
# print(int_to_mini_roman(426))
# print(int_to_mini_roman(1969))
