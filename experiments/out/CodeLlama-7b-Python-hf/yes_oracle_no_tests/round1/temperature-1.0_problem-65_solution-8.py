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

    l = str ( x )
    s = l
    # Shift
    if shift < 0:
        s = s[:shift] + ''.join(reversed (list (s[-shift:])))
    else:
        s = s[shift:] + s[:shift]

    return s


if __name__ == "__main__":
    import doctest
    doctest.testmod()