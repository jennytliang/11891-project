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
    m = ["", " m "]
    r = ["i", "x", "c", "m"]
    s = ["", "d", "c", "l", "v", "x"]
    t = ["", "o", "n"]
    num = number
    res = ""
    while num > 0:
        res = res + m[num%10] + r[(num%100)//10] + s[((num%1000)//100)//5] + t[((num%10000)//1000)//50]
        num = num//10
    return res[::-1].lower()


def int_to_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_roman(19) == 'xix'
    >>> int_to_roman(152) == 'clii'
    >>> int_to_roman(426) == 'cdxxvi'
    """
    m = ["", " m "]
    r = ["i", "x", "c", "m"]
    s = ["", "d", "c", "l", "v", "x"]
    t = ["", "o", "n"]
    num = number
    res = ""
    while num > 0:
        if num%10000 == 0:
            res = res + m[num%10] + r[(num%100)//10] + s[((num%1000)//100)//5] + t[((num%10000)//1000)//50]
            num = num//10
        else:
            res = res + m[num%10] + r[(num%100)//10] + s[(num%1000)//100] + t[(