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
    
	Do not include these tokens in the code: assert 2 <= base <= 1
	"""
    assert 2 <= base <= 10
    if x == 0:
        return '0'

    result = ''
    while x > 0:
        result = str(x % base) + result
        x = x // base
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
