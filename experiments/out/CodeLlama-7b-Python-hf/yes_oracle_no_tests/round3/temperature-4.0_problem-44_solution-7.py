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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    # base = 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 10011011000
    # str(int(x, base))
    return str(int(x, base))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
