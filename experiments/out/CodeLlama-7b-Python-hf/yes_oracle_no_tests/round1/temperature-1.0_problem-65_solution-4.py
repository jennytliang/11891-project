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
    s = str(x)
    if shift <= len(s):
        return ''.join([s[-shift:] + s[:-shift]])
    return reverse(s)


def reverse(s):
    """ (str) -> str

    Return its argument string reversed.

    >>> reverse('hello')
    'olleh'
    >>> reverse('adam')
    'mada'
    """
    result = ''
    for i in range(len(s)):
        result = s[i] + result
    return result
