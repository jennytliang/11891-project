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
 	    return '0'
    if x < 0:
        raise ValueError('x must be positive')
    if base < 2:
        raise ValueError('base must be greater than or equal to 2')
    if base > 10:
        raise ValueError('base must be less than or equal to 10')

    result = ''
    while x > 0:
        digit = x % base
        if digit >= 10:
            digit = chr(ord('A') + digit - 10)
        result = str(digit) + result
        x = x // base
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
