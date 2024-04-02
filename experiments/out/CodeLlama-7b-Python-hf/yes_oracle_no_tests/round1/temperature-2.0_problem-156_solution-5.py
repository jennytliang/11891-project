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
    d = ["", "d", "cd", "ccc", "dcc", "c", "cl", "l", "lx", "xc", "lxc", "x", "xl", "xcx", "cx", "cxx"]
    t = ["", "t", "tw", "th", "ft", "f", "fti", "fi", "ftii", "ii"]
    h = ["", "h", "hg", "hhg", "hgg", "hg", "hgw", "hw", "hgwg", "hwg", "hgwgg", "hgg", "hgwg", "hwg", "hgww", "w"]
    s = ["", "s", "sc", "ssc", "scc", "s", "si", "sii"]
    g = ["", "g", "gg", "ggg"]
    g_mod = ["", "g", "gg", "ggg"]

    def roman_num(number):
        if number < 4:
            return d[number]
        elif number == 4:
            return "c"
        elif number == 5:
            return "v"
        elif number < 9:
            return t[number-5]
        elif number == 9:
            return "x"
        elif number < 40:
            return h[number-10]
        elif number == 40:
            return "l"
        elif number < 100:
            return s[number-50]
        elif number == 100:
            return "c"
        elif number < 500:
            return g[number//100]
        elif number == 500:
            return "d"
        elif number < 1000:
            return g_mod[number//500]

    def get_roman(number):
        if number < 1000:
            return roman_num(number % 10) + roman_num(number // 10)
        else: