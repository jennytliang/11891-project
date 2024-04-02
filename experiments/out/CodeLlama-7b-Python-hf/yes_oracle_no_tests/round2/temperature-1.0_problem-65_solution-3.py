def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s = str ( x ) if shift
	"""

    # If shift is 0, return string version of x, i.e. the empty string ""
    if shift == 0:
	    return ""
    
    # String version of x
    s = str(x)
    
    # Return the reverse of the original substring if shift > number of digits
    if len(s) - shift < 0:
        return s[::-1]

    # Otherwise return substring ending at digit shift away from beginning 
    return s[shift:] + s[:shift]