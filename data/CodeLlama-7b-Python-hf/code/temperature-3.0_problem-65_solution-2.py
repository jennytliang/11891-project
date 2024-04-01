def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if not shift: return str(x)
    if len(str(x)) <= shift: return ''.join(reversed(str(x)))
    s = list(str(x))
    s = s[-shift:]+s[:-shift]
    return ''.join(s)
print(circular_shift(2134, 4))
