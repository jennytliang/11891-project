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
    x = ["", "x", "xx", "xxx", "l", "ll", "lll", "llll", "c", "cc", "ccc", "cccc", "d", "dd", "ddd", "dddd", "v", "vv", "vvv", "vvvv", "u", "uu", "uuu", "uuuu", "i", "ii", "iii", "iiii", "t", "tt", "ttt", "tttt", "j", "jj", "jjj", "jjjj"]
    if number < 1 or number > 1000:
        return "Out of range"
    else:
        return m[number // 1000] + x[number % 1000 // 100] + m[number % 100 // 10] + x[number % 10]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
