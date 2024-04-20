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
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(reversed(digits))

if __name__ == '__main__':
    import doctest
    doctest.testmod()