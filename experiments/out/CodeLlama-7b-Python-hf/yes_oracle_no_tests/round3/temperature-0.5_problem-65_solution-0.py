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
        ret = s[::-1]
    else:
        shift = shift % len(s)
        ret = s[shift:] + s[:shift]
    return ret


def circular_shift_2(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    s = str(x)
    if shift > len(s):
        ret = s[::-1]
    else:
        shift = shift % len(s)
        ret = s[shift:] + s[:shift]
    return ret







def main():
    import doctest
    doctest.testmod()
    print(circular_shift(12, 1))
    print(circular_shift(12, 2))
    print(circular_shift(123456789, 4))
    print(circular_shift(123456789, 10))
    print(circular_shift(123456789, 11))
    print(circular_shift(123456789, 12))


if __name__ == '__main__':
    main()