def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: shift >
	"""

    s = str(x)
 
    if shift > len(s):
        return s[::-1]
    return s[shift:] + s[:shift]

    #if shift > len(s):
    #    return s[::-1]
    #return s[shift:] + s[:shift]


def main():
    print(circular_shift(12, 1))
    print(circular_shift(12, 2))
    print(circular_shift(1234, 2))
    print(circular_shift(1234, 6))
    print(circular_shift(1234, 8))


if __name__ == "__main__":
    main()
