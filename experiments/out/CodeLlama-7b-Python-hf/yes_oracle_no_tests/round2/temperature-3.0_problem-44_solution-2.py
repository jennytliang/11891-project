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
    
	Include these tokens in the code: if x ==
	"""
    if x < 0:
        # The absolute value of x is used in order to be compatible
        # with the next if statement
        x = abs(x)
        sign = -1
    elif x == 0:
        sign = 0
    else:
        sign = 1
    if x == 0:
        return '0'
    res = ''
    while x:
        res = str(x % base) + res
        x //= base
    if sign < 0:
        res = '-' + res
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()