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
    
	Do not include these tokens in the code: 
	"""

    if x == 0:
 	    return '0'
    elif x < 0:
        return '-' + change_base(-x, base)
    else:
        return num_to_str(x, base)


def num_to_str(x: int, base: int = 10):
    """Return string representation of x in the given base.
    >>> num_to_str(5, 2)
    '101'
    >>> num_to_str(5, 8)
    '5'
    >>> num_to_str(5, 16)
    '5'
    """
    if x == 0:
        return ''
    else:
        return num_to_str(x // base, base) + str(x % base)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
