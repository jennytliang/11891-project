def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Do not include these tokens in the code: 0 <
	"""


    s = str(x)
    if len(s) > shift:
        return s[-shift:] + s[:-shift]
    else:
        return s[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()