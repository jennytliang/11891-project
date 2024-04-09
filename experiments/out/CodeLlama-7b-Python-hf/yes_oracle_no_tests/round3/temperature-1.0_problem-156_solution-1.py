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
    s = ""
    for i in str(number):
        i = int(i)
        if i < 4:
            for j in range(i):
                s += m[j % 2]
        elif i == 4:
            s += "".join(m)
        elif i < 9:
            s += m[1] + m[0] * (i - 5)
        else:
            s += m[1] + "".join(m)
    return s.replace(" ", "")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
