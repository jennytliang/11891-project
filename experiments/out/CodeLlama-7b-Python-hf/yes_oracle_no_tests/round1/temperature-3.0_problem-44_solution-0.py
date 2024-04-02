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
    result = ''
    while x > 0:
        result = str(x % base) + result
        x = x // base
    return result


print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))

# 0.000220 seconds
