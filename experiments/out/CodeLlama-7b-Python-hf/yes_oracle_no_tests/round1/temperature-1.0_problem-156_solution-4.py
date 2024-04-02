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

    m = ["I", "X", "C", "M", "V", "L", "D", ""]
    k = [1000, 900,  500, 400, 100,  90,  50, 40,  10,  9,   5, 4, 1]
    
    res = ''
    for i in (0, len(k)-1):
        res += [m[i+1], m[i]][number//k[i]]*[number//k[i],  1][i==0]
        number %= k[i]

    return res.lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()