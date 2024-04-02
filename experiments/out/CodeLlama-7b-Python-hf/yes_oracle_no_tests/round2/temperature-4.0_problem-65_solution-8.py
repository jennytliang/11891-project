def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len ( s ) if
	"""

    s = str(x)
    if shift > len(s):
        retur s[::-1]
    else:
        return s[shift:] + s[:shift]


print(circular_shift(12, 1))
print(circular_shift(12, 2))
