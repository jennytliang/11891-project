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
    base_str = '0123456789ABCDEF'
    if x == 0:
        return '0'
    res = ''
    while x:
        res += base_str[x % base]
        x //= base
    return res[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
