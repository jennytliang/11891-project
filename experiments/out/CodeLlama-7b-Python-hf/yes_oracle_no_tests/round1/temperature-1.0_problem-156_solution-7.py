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
    num = number
    result = ""
    while num > 0:
        if num >= 1000:
            result += "m"
            num -= 1000
        elif num >= 900:
            result += "cm"
            num -= 900
        elif num >= 500:
            result += "d"
            num -= 500
        elif num >= 400:
            result += "cd"
            num -= 400
        elif num >= 100:
            result += "c"
            num -= 100
        elif num >= 90:
            result += "xc"
            num -= 90
        elif num >= 50:
            result += "l"
            num -= 50
        elif num >= 40:
            result += "xl"
            num -= 40
        elif num >= 10:
            result += "x"
            num -= 10
        elif num >= 9:
            result += "ix"
            num -= 9
        elif num >= 5:
            result += "v"
            num -= 5
        elif num >= 4:
            result += "iv"
            num -= 4
        elif num >= 1:
            result += "i"
            num -= 1
    return result[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
