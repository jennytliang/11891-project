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
    d = ["", "d", "cd", "ccc", "c", "l", "lx", "lxx", "lxxx", "xc"]
    c = ["", "c", "cc", "ccc", "c", "d", "dc", "dcc", "dccc", "c"]
    x = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "x"]
    v = ["", "v", "vc", "ccc", "c", "d", "dc", "dcc", "dccc", "c"]
    u = ["", "u", "uc", "ccc", "c", "v", "vc", "vcc", "vccc", "c"]
    t = ["", "t", "tc", "ccc", "c", "u", "uc", "ucc", "uccc", "c"]
    s = ["", "s", "sc", "ccc", "c", "t", "tc", "tcc", "tccc", "c"]
    int_to_mini_roman_map = [m, c, x, v, u, t, s]

    roman_num = ""
    for i in range(len(int_to_mini_roman_map)):
        roman_num += int_to_mini_roman_map[i][(number // (10**i))]
        number %= (10**i)

    return roman_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
