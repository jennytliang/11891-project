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
    c = ["", " c ", " cc ", " ccc ", " cd ", " dc ", " dcc ", " dccc ", " cm "]
    x = ["", " x ", " xx ", " xxx ", " xl ", " lx ", " lxx ", " lxxx ", " xc "]
    i = ["", " i ", " ii ", " iii ", " iv ", " v ", " vii ", " viii ", " ix "]
    return "".join(i[number % 10] + x[number % 50 // 10] + c[number % 100 // 10] + m[number % 1000 // 1000])



































































































































































































































































































































