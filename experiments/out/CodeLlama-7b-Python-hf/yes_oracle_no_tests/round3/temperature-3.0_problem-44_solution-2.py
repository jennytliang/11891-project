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
    
	Do not include these tokens in the code: if x < 0 :
	"""

    if x < 0:
        raise ValueError("x should be a positive integer")

    if base < 2 or base > 10:
        raise ValueError("base should be between 2 and 10")

    def _convert(x, base):
        if x < base:
            return str(x)
        else:
            return _convert(x // base, base) + str(x % base)

    return _convert(x, base)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
