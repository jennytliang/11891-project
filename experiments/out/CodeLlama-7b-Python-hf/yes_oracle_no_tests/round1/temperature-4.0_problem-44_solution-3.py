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
    num_list = []
    while x:
        num_list.append(x % base)
        x = x // base
    return ''.join(map(str, num_list[::-1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()