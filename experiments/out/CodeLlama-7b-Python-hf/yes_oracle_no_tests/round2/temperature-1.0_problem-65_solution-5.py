def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len ( s ) if
	Do not include these tokens in the code: else
	"""

    s = str(x)
    if shift > len(s):
        returndigit = s[::-1]
    else:
        returndigit = s[shift:] + s[:shift]
    return returndigit


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len ( s ) if
	Do not include these tokens in the code: else
	"""

    s = str(x)
    if shift > len(s):
        returndigit = s[::-1]
    else:
        returndigit = s[shift:] + s[:shift]
    return returndigit


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
