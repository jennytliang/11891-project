def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    
	Include these tokens in the code: "
	Do not include these tokens in the code: '
	"""

    if x == 0:
 	    return "0"
 	
    # base = 0
    # while x > 0:
    #     base = x % 10 + base * 10
    #     x = x // 10
    # return str(base)

    # return str(x)

    # if x == 0:
    #     return "0"
    #
    # base = 0
    # while x > 0:
    #     base = x % 10 + base * 10
    #     x = x // 10
    # return str(base)

    # if x == 0:
    #     return "0"
    #
    # base = 0
    # while x > 0:
    #     base = x % 10 + base * 10
    #     x = x // 10
    # return str(base)

    if x == 0:
        return "0"

    base = 0
    while x > 0:
        base = x % base + base * 10
        x = x // 10
    return str(base)


if __name__ == "__main__":
    import doctest
    doctest.testmod()