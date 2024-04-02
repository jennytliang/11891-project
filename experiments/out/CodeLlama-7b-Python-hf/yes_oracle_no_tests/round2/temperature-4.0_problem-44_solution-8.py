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
    # YOUR CODE HERE
    # raise NotImplementedError
    res = ''
    while x != 0:
        res = str(x % base) + res
        x = x//base
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
