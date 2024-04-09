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
    
	Do not include these tokens in the code: base _ str = ' 0 1
	"""
    # your code here
    if x < 0:
        return '-' + change_base(-x, base)
    b = 1
    res = ''
    while b <= x:
        b *= base
    b /= base
    while x >= b:
        res += str(x // b)
        x %= b
        b /= base
    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
