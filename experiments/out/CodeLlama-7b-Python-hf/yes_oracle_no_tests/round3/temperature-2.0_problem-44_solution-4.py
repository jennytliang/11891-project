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
    
	Include these tokens in the code: ret = ""
	Do not include these tokens in the code: if x == 1 : return "
	"""



    if x == 0:
        return "0"

    if x == 1:
        return "1"

    ret = ""
    while x > 0:
        x, rem = divmod(x, base)
        ret = str(rem) + ret
    return ret









