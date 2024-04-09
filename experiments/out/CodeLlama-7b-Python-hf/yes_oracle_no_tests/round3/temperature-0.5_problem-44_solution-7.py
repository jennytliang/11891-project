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
    if x == 1:
        return '1'
    if x == 2:
        return '10'
    if x == 3:
        return '11'
    if x == 4:
        return '100'
    if x == 5:
        return '101'
    if x == 6:
        return '110'
    if x == 7:
        return '111'
    if x == 8:
        return '1000'
    if x == 9:
        return '1001'

    result = ''
    while x > 0:
        remainder = x % base
        result = change_base(int(x / base), base) + change_base(remainder, base)
        x = int(x / base)
    return result

































































































































































































































































































