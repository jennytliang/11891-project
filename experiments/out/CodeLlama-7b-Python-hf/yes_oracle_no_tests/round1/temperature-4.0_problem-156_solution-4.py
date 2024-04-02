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
    out = ''
    while number > 0:
        if number >= 1000:
            out = 'm' + out
            number -= 1000
        elif number >= 500:
            out = 'd' + out
            number -= 500
        elif number >= 100:
            out = 'c' + out
            number -= 100
        elif number >= 50:
            out = 'l' + out
            number -= 50
        elif number >= 10:
            out = 'x' + out
            number -= 10
        elif number >= 5:
            out = 'v' + out
            number -= 5
        elif number >= 1:
            out = 'i' + out
            number -= 1
    return out.replace(" ", "").lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()