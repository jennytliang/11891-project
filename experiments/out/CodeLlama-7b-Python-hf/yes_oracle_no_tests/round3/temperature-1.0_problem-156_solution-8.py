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
    num = number
    a = []
    while num > 0:
        num, d = divmod(num, 10)
        if d == 5:
            a.append("v")
            a.append(m[d%10])
        elif d < 5:
            a.append(m[d])
            if d > 0:
                a.append("v")
        else:
            a.append("x")
            if d > 1:
                a.append(m[d-5])
            else:
                a.append(m[d%10])
    return "".join(a)


if __name__ == "__main__":
    import doctest
    doctest.testmod()