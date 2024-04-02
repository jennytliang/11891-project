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

    mr = ""
    while number > 0:
        if number >= 1000:
            mr += "m"
            number -= 1000
        elif number >= 900:
            mr += "cm"
            number -= 900
        elif number >= 500:
            mr += "d"
            number -= 500
        elif number >= 400:
            mr += "cd"
            number -= 400
        elif number >= 100:
            mr += "c"
            number -= 100
        elif number >= 90:
            mr += "xc"
            number -= 90
        elif number >= 50:
            mr += "l"
            number -= 50
        elif number >= 40:
            mr += "xl"
            number -= 40
        elif number >= 10:
            mr += "x"
            number -= 10
        elif number >= 9:
            mr += "ix"
            number -= 9
        elif number >= 5:
            mr += "v"
            number -= 5
        elif number >= 4:
            mr += "iv"
            number -= 4
        elif number >= 1:
            mr += "i"
            number -= 1
    return mr


if __name__ == "__main__":
    import doctest
    doctest.testmod()
