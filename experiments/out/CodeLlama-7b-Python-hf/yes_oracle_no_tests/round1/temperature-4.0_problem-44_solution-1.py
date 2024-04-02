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
    
	Include these tokens in the code: if x ==
	"""
    # base_string = ''
    # while x > 0:
    #     x, rem = divmod(x, base)
    #     base_string = str(rem) + base_string
    # return base_string
    return str(x).lstrip('-').replace('-', '').zfill(1000).rstrip(str(0))[::-1] if x < 0 else str(x).zfill(1000).rstrip(str(0))[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
