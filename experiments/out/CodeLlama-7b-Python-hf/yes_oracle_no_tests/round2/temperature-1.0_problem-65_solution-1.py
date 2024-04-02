def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: >
	Do not include these tokens in the code: <
	"""

    s = str(x)
    if 0 < shift and shift < len(s) or shift < 0:
        s = s[-shift:] + s[:-shift]
    return s

for i in range(200):
    j = 5 + 3 - i*2
    print(circular_shift(i, -j), circular_shift(i, -j) == str(i).__reversed__())