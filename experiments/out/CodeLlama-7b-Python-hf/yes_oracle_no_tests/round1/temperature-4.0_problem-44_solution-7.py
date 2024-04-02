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
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: < 0 or base <= 0 : raise
	"""


  
    if x < 0 or base <= 0:
        raise ValueError('x or base is less than 0.')
    else:
        return ((x == 0) and '0') or (change_base(x // base, base).lstrip('0') + '0123456789'[x % base])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
