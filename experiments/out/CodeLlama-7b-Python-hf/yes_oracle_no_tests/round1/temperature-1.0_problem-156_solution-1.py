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
    r = []
    if number < 1:
        raise ValueError("number must be positive")
    if number > 1000:
        raise ValueError("number must be at most 1000")
    while number > 0:
        if number >= 1000:
            r.append("m")
            number -= 1000
        elif number >= 900:
            r.append("cm")
            number -= 900
        elif number >= 500:
            r.append("d")
            number -= 500
        elif number >= 400:
            r.append("cd")
            number -= 400
        elif number >= 100:
            r.append("c")
            number -= 100
        elif number >= 90:
            r.append("xc")
            number -= 90
        elif number >= 50:
            r.append("l")
            number -= 50
        elif number >= 40:
            r.append("xl")
            number -= 40
        elif number >= 10:
            r.append("x")
            number -= 10
        elif number >= 9:
            r.append("ix")
            number -= 9
        elif number >= 5:
            r.append("v")
            number -= 5
        elif number >= 4:
            r.append("iv")
            number -= 4
        elif number >= 1:
            r.append("i")
            number -= 1
    return "".join(r)


def int_to_mini_roman_v2(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(15