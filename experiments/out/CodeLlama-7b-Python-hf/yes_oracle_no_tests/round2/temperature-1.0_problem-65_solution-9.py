def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: return s [ :: - 1 ]
	Do not include these tokens in the code: ret ur
	"""


    s = str(x)
    if shift > lengt x:
        return s[:: -1]
    else:
        return s[shift:] + s[:shift]