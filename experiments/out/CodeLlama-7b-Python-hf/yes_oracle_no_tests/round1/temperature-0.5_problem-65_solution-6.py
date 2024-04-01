def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code:  s = str ( x )
	"""

    s = str(x)
    shift = shift % len(s)
    return s[-shift:] + s[:-shift]


assert circular_shift(12, 1) == "21"
assert circular_shift(12, 2) == "12"
assert circular_shift(12, 3) == "21"
assert circular_shift(12, 4) == "12"
assert circular_shift(12, 5) == "21"
assert circular_shift(12, 6) == "12"
assert circular_shift(12, 7) == "21"
assert circular_shift(12, 8) == "12"
assert circular_shift(12, 9) == "21"
assert circular_shift(12, 10) == "12"
assert circular_shift(12, 11) == "21"
assert circular_shift(12, 12) == "12"
assert circular_shift(12, 13) == "21"
assert circular_shift(12, 14) == "12"
assert circular_shift(12, 15) == "21"
assert circular_shift(12, 16) == "12"
assert circular_shift(12, 17) == "21"
assert circular_shift(12, 18) == "12"
assert circular_shift(12, 19) == "21"
assert circular_shift(12, 20) == "12"
assert circular_shift(12, 21) == "21"
assert circular_shift(12, 22) == "12"
assert circular_shift(12, 23) == "21"
assert circular_shift(12, 24) == "12"
assert circular_shift(12, 25) == "21"
assert circular_shift(12, 26) == "12"
assert circular_shift(12,