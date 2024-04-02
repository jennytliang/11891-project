def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: if
	"""


    s = str(x)
    if shift <= len(s):
        return s[shift:] + s[:shift]
    else:
        return s[shift:] + s[:shift][::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(circular_shift(12, 1))
    print(circular_shift(12, 2))