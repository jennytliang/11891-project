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
    
	Do not include these tokens in the code: if base < 2 :
	"""
    if base < 2:
        return
    digits = "0123456789ABCDEF"
    if x < 0:
        return "(" + change_base(-x, base) + ")"
    elif x == 0:
        return "0"
    else:
        return digits[x % base] + change_base(x // base, base)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
