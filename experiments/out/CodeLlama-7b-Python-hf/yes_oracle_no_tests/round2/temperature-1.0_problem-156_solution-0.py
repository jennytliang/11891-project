def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: m "] c = [" ", " c
	"""

    m = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    t = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    
    result = ""
    for i in range(len(m)):
        count = number // m[i]
        result += str(t[i]) * count
        number -= m[i] * count
    return result.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
