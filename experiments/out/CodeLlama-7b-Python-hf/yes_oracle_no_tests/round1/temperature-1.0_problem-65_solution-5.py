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
	size = len(str(x))
	if shift > size or shift == 0:
		return str(x)
    for i in xrange(1,shift+1):
	str_x = str(x)
	last_dig = str_x[-1]
	str_x = str_x[:-1]
	str_x = last_dig + str_x
    return str_x

print circular_shift (12345, 2)
print circular_shift (54321, 3)
print circular_shift (12, 5)
