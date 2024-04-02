def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s = str ( x )
	"""
    s = str(x)
    if len(s) <= shift:
        return s[::-1]
    else:
        return s[shift:] + s[:shift]


def circular_shift2(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Use the built-in function str to convert x to a string.
	"""
    s = str(x)
    return s[-shift:] + s[:-shift]
