def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 0:
        return "-" + circular_shift(-x, shift)
    elif x == 0:
        return "0"
    else:
        digits = []
        while x > 0:
            digits.append(str(x % 10))
            x = x // 10
        if shift > len(digits):
            return ''.join(reversed(digits))
        else:
            return ''.join(digits[-shift:] + digits[:-shift])


if __name__ == '__main__':
    import doctest
    doctest.testmod()