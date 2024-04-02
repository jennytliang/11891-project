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
    d = ["i", "x", "c", "m"]
    r = []
    for i in range(4):
        r.append(number % 10)
        number = number // 10
    for i in range(4):
        if r[i] == 1:
            r[i] = d[i]
        elif r[i] == 2:
            r[i] = d[i] + d[i]
        elif r[i] == 3:
            r[i] = d[i] + d[i] + d[i]
        elif r[i] == 4:
            r[i] = d[i - 1] + d[i]
        elif r[i] == 5:
            r[i] = d[i - 1]
        elif r[i] == 6:
            r[i] = d[i - 1] + d[i] + d[i]
        elif r[i] == 7:
            r[i] = d[i - 2] + d[i]
        elif r[i] == 8:
            r[i] = d[i - 2] + d[i] + d[i]
        elif r[i] == 9:
            r[i] = d[i - 2] + d[i - 1] + d[i]
    r = [x for x in r if x != 0]
    return m[0] + m[1].join(r)
