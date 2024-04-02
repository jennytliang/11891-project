def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Do not include these tokens in the code: # Base Case
	"""

    s = str(x)
    return s[shift%len(s):] + s[:shift%len(s)]

    # another version
    # import math
    # return (str(-(x % (10*int(math.floor(math.log10(abs(x))))) + 10))[1:] +
    #         str(abs(x)))[::-1][:len(str(abs(x)))]