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
    t = ["", "d", "c", "l", "x", "v", "i"]
    result = ""
    for i in range(1, 8):
        if number >= 10 ** i:
            result += t[i] * (number // (10 ** i))
            number = number % (10 ** i)
    result += t[0] * number
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
