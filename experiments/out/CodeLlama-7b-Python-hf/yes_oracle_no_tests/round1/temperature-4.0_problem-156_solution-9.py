def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m = [" ", " m "] c
	"""
    m = [" ", " m "]
    c = ["", "d", "c", "m"]
    x = ["", "x", "l", "v"]
    i = ["", "i", "x", "i"]
    ans = ""
    if number < 1:
        return ""
    while number > 0:
        if number >= 1000:
            ans += "m"
            number -= 1000
        elif number >= 900:
            ans += "cm"
            number -= 900
        elif number >= 500:
            ans += "d"
            number -= 500
        elif number >= 400:
            ans += "cd"
            number -= 400
        elif number >= 100:
            ans += "c"
            number -= 100
        elif number >= 90:
            ans += "xc"
            number -= 90
        elif number >= 50:
            ans += "l"
            number -= 50
        elif number >= 40:
            ans += "xl"
            number -= 40
        elif number >= 10:
            ans += "x"
            number -= 10
        elif number >= 9:
            ans += "ix"
            number -= 9
        elif number >= 5:
            ans += "v"
            number -= 5
        elif number >= 4:
            ans += "iv"
            number -= 4
        elif number >= 1:
            ans += "i"
            number -= 1
    return ans


def int_to_mini_roman(number):
    m = [" ", " m "]
    c = ["", "d", "c", "m"]
    x = ["", "x", "l", "v"]
    i = ["", "i", "x", "i"]
    ans = ""
    if number < 1:
        return ""
    while number > 0:
        if number >= 1000:
            ans += "m"