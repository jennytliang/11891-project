def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Include these tokens in the code: ",
	"""

    m = {1:"c", 5:"l", 10:"x", 50:"xc", 100:"c", 500:"l", 1000:"d"}
    return "".join([m[i] for i in sorted(m.keys(), reverse=True) if i <= number])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
