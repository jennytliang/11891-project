def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: return
	Do not include these tokens in the code: ret ur =
	"""


    s = str(x)
    if shift > l:
        return s[::-1]
    else:
        return s[shift:] + s[:shift]


def reverse_string(string):
    """Reverse the given string and return it as a new string.
    Do not use the built-in function reversed.

    >>> reverse_string('abc')
    'cba'
    >>> reverse_string('a')
    'a'
    >>> reverse_string('ab')
    'ba'
    """

    # for i in range(len(string)):
    #     s = s + string[len(string) - 1 - i]
    # return s

    return string[::-1]


def reverse_string2(string):
    """Same as previous, but use slicing instead of explicit indexing.

    >>> reverse_string2('abc')
    'cba'
    >>> reverse_string2('a')
    'a'
    >>> reverse_string2('ab')
    'ba'
    """

    return string[::-1]


def reverse_string3(string):
    """Same as previous, but use extended slice syntax.

    >>> reverse_string3('abc')
    'cba'
    >>> reverse_string3('a')
    'a'
    >>> reverse_string3('ab')
    'ba'
    """

    return string[::-1]


def reverse_string4(string):
    """Same as previous, but use a recursive solution."""

    if len(string) == 0:
        return ""
    else:
        return reverse_string4(string[1:]) + string[0]


def reverse_string5(string):
    """Same as previous, but use a recursive solution."""

    if len(string) == 0:
        return ""
    else:
        return string[-1] + reverse_string5(string[:-1])


def reverse_string6(string):
    """Same as previous, but use a recursive solution."""

    if len(string) == 0: