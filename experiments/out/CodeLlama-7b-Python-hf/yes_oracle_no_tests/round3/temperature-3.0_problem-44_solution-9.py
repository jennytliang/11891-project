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
 
        return 0

    base_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base_len = len(base_str)

    if base_len <= base:
        raise Exception("base is larger than the base length.")

    if x < 0:
        x = -x
        sign = -1
    else:
        sign = 1

    result = ""
    while x != 0:
        result = base_str[x % base] + result
        x = x // base

    if sign == -1:
        result = "-" + result

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
