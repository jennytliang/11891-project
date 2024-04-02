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
    d = [" ", " d "]
    t = [" ", " t "]
    c = [" ", " c "]
    l = [" ", " l "]
    x = [" ", " x "]
    v = [" ", " v "]
    i = [" ", " i "]
    return "".join(
        [
            m[number % 1000 // 1000],
            d[number % 100 // 100],
            t[number % 100 // 10],
            c[number % 10],
        ]
    )
