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

    res = []
    for _ in range(0, 101):
        if len(res) != 0 and x < base**(len(res) - 1):
            return ''.join([str(c) for c in reversed(res)])

        res.append(x % base)
        x //= base

    return ''.join([str(c) for c in reversed(res)])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)