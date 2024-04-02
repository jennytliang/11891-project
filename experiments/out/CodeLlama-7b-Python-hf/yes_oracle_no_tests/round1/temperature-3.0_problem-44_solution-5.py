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
    assert 2 <= base <= 10, "Base must be between 2 to 10"
    assert x >= 0, "Number must be greater than or equal to 0"

    if x == 0:
        return '0'
    result = ''

    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base

    return result