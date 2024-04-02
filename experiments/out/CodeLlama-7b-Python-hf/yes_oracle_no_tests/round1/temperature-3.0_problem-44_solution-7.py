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
    # your code here
    output = ''
    while x > 0:
        output = str(x % base) + output
        x = x // base
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
