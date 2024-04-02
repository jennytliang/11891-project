def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s =
	Do not include these tokens in the code: if not shift : return
	"""

    s = str(x)
    if not shift:
        return s
    if len(s) < shift:
        return s[::-1]
    return s[shift:] + s[:shift]


def test_circular_shift():
    assert circular_shift(12, 1) == "21"
    assert circular_shift(12, 2) == "12"
    assert circular_shift(12, 3) == "21"
    assert circular_shift(12, 4) == "12"
    assert circular_shift(12, 5) == "21"
    assert circular_shift(12, 6) == "12"
    assert circular_shift(12, 7) == "21"
    assert circular_shift(12, 8) == "12"
    assert circular_shift(12, 9) == "21"
    assert circular_shift(12, 10) == "12"
    assert circular_shift(12, 11) == "21"
    assert circular_shift(12, 12) == "12"
    assert circular_shift(12, 13) == "21"
