def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: len ( s ):
	Do not include these tokens in the code: l :
	"""



    s = str(x)
    if 0 < shift < len(s):
        return s[shift:] + s[:shift]
    elif shift >= len(s):
        return s[::-1]
    else:
        return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
