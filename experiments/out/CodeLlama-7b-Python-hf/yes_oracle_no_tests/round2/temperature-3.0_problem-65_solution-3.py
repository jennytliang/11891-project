def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Do not include these tokens in the code: not
	"""

    s = str(x)
 
    # TODO: your code here
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s)-shift:] + s[:len(s)-shift]


def main():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
