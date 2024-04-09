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
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r = ""
    for c in str(number):
        if int(c) < d[r[-1]]:
            r += m[0]
        else:
            r += m[1]
        r += c
    return r.lower()


def mini_roman_to_int(string):
    """
    Given a string, obtain its integer equivalent.
    Restrictions: 1 <= len(string) <= 10

    Examples:
    >>> mini_roman_to_int('xix') == 19
    >>> mini_roman_to_int('clii') == 152
    >>> mini_roman_to_int('cdxxvi') == 426
    """
    s = string.upper()
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r = 0
    for i in range(len(s)):
        if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
            r -= d[s[i]]
        else:
            r += d[s[i]]
    return r
