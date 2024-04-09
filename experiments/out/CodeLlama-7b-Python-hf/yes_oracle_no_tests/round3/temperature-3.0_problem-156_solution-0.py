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
    number = int(number)
    if number > 1000 or number < 1:
        raise ValueError('Please input a number between 1 and 1000')

    if number == 1000:
        return 'm'
    elif number >= 900:
        return 'cm' + int_to_mini_roman(number - 900)
    elif number >= 500:
        return 'd' + int_to_mini_roman(number - 500)
    elif number >= 400:
        return 'cd' + int_to_mini_roman(number - 400)
    elif number >= 100:
        return 'c' + int_to_mini_roman(number - 100)
    elif number >= 90:
        return 'xc' + int_to_mini_roman(number - 90)
    elif number >= 50:
        return 'l' + int_to_mini_roman(number - 50)
    elif number >= 40:
        return 'xl' + int_to_mini_roman(number - 40)
    elif number >= 10:
        return 'x' + int_to_mini_roman(number - 10)
    elif number >= 9:
        return 'ix' + int_to_mini_roman(number - 9)
    elif number >= 5:
        return 'v' + int_to_mini_roman(number - 5)
    elif number >= 4:
        return 'iv' + int_to_mini_roman(number - 4)
    else:
        return 'i' + int_to_mini_roman(number - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
