def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s =
	Do not include these tokens in the code: if not shift : return
	"""
    s = str(x)
    if not shift:
        return s
    return s[shift:] + s[:shift]


# print(circular_shift(1234, 1))
# print(circular_shift(1234, 2))
# print(circular_shift(1234, 3))
# print(circular_shift(1234, 4))