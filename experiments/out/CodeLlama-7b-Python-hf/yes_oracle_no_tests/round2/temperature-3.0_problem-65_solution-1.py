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
        retur = s[::-1]
    else:
        retur = s[shift:] + s[:shift]

    return retur


#print(circular_shift(12, 1))
#print(circular_shift(12, 2))



def circular_shift_2(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_2(12, 1)
    "21"
    >>> circular_shift_2(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len ( s ) if
	Do not include these tokens in the code: else
	"""

    s = str(x)
    retur = s[shift:] + s[:shift]

    return retur


#print(circular_shift_2(12, 1))
#print(circular_shift_2(12, 2))



def circular_shift_3(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift_3(12, 1)
    "21"
    >>> circular_shift_3(12, 2)
    "12"
    
	Include these tokens in the code: shift % = len ( s ) if
	Do not include these tokens in the code: else
	"""

    s = str(x)
    retur = s[shift % len(s):] + s[:shift % len(s)]

    return retur


#print(circular_shift_3(12, 1))
#print(circular_shift_3(12, 2))



def circular_shift_4(x, shift):
    """Circular shift the digits of the integer x,