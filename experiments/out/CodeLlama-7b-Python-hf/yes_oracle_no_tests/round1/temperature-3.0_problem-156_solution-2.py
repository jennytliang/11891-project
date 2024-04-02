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
    # Your code here
    m = [" ", " m "]
    x = ["i","x","c","m"]
    d = [1,10,100,1000]
    r = ""
    for i in range(len(x)):
        while number >= d[i]:
            r += x[i]
            number -= d[i]
    return r.lower()


if __name__ == "__main__":
    import doctest
    doctest.testmod()