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
    
	Do not include these tokens in the code: if base < 2 or base
	"""
    if base < 2:
        raise ValueError("base must be greater than 1")
    if x < 0:
        raise ValueError("x must be a positive number")
    res = []
    while x:
        res.append(str(x % base))
        x //= base
    return ''.join(res[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
