def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    
	Do not include these tokens in the code: ", " m " ] n = ["
	"""

    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = ["", "m", "mm", "mmm"]
    return n[number // 1000] + n[(number % 1000) // 100] + n[(number % 100) // 10] + n[number % 10]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
