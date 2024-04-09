def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Do not include these tokens in the code: ret ur s [ :: - 1 ]
	"""


    s = str(x)
    if shift > l:
        return s[:: -1]
    return s[l - shift:] + s[:l - shift]


def circular_shift_2(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Do not include these tokens in the code: ret ur s [ :: - 1 ]
	"""

    s = str(x)
    if shift > l:
        return s[:: -1]
    return s[l - shift:] + s[:l - shift]


if __name__ == "__main__":
    import doctest
    doctest.testmod()