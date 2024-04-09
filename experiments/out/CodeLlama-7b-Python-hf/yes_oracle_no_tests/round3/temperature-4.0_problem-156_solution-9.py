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
    m = ["I", "V", "X", "L", "C", "D", "M"]
    c = [1000, 500, 100, 50, 10, 5, 1]
    s = ""
    for i in range(len(c)):
        while number >= c[i]:
            s += m[i]
            number -= c[i]
    return s.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
