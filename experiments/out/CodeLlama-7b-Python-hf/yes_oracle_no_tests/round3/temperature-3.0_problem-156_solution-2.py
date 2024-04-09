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
    d = {1: "i", 5: "v", 10: "x"}
    t = {1: "i", 10: "x"}
    result = ""
    for key in sorted(d.keys(), reverse=True):
        while number >= key:
            result += d[key]
            number -= key
    for key in sorted(t.keys(), reverse=True):
        while number >= key:
            result += t[key]
            number -= key
    return result.lower()
