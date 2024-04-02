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
    s = str ( x )
    shift = shift % len ( s )
    return s [ shift : ] + s [ : shift ]
    


def main():
    import doctest
    doctest.testmod()
    print(circular_shift(123456789, 8))
    print(circular_shift(123456789, 2))
    print(circular_shift(123456789, 12))

if __name__ == "__main__":
    main()