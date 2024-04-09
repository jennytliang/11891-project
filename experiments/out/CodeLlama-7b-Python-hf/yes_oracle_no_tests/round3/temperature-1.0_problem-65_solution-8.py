def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len
	Do not include these tokens in the code: return s [ :] + s [: ]
	"""


    s = str(x)

    if shift > len(s):
        ret = s[::-1]
    else:
        ret = s[shift:] + s[:shift]

    return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(circular_shift(12, 1))
    print(circular_shift(12, 2))
    print(circular_shift(12, 3))
    print(circular_shift(12, 4))
    print(circular_shift(12, 5))
    print(circular_shift(12, 6))
    print(circular_shift(12, 7))
    print(circular_shift(12, 8))
    print(circular_shift(12, 9))
    print(circular_shift(12, 10))
    print(circular_shift(12, 11))
    print(circular_shift(12, 12))
    print(circular_shift(12, 13))
    print(circular_shift(12, 14))
    print(circular_shift(12, 15))
    print(circular_shift(12, 16))
    print(circular_shift(12, 17))
    print(circular_shift(12, 18))
    print(circular_shift(12, 19))
    print(circular_shift(12, 20))
    print(circular_shift(12, 21))
    print(circular_shift(12, 22))
    print(circular_shift(12, 23))
    print(circular_shift(12, 24))
    print(circular_shift(12, 25))
    print(circular_shift(12, 26))
    print(circular_shift(12, 27))
    print(circular_shift(12, 28))
    print(circ