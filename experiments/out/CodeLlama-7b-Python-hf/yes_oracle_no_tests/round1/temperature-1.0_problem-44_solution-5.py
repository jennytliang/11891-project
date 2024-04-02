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
 		return "0"
    elif x == 1:
		return "1"
    elif (x > base):
		base_s = change_base(x // base, base)
		return base_s + change_base(x % base, base)
    else:
		return str(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
