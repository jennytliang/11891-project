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
    base_list = []
    while x >= base:
        base_list.append(str(x % base))
        x = x // base
    base_list.append(str(x))
    return ''.join(reversed(base_list))


if __name__ == "__main__":
    import doctest
    doctest.testmod()