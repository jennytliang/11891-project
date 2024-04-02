def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: (
	"""

    s  = '123456789'
    re = '987654321'
    # code goes here
    if x < 0:
    	x = -x
    if shift > len(str(x)):
        return re[shift: len(str(x)) + shift] + re[0 : shift] 
    return s[shift: len(str(x)) + shift] + s[0 : shift]