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

    m = {
        1000 : "m",
        500 : "d",
        100 : "c",
        50 : "l",
        10 : "x",
        5 : "v",
        1 : "i"
    }

    # your code here
    result = []
    for key in m:
        if key <= number:
            number -= key
            result.append(m[key])
    return "".join(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()