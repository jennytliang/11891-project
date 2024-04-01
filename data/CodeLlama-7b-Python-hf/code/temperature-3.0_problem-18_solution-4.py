def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    return string.count(substring)


def can_be_divided(number: int, parts: int) -> bool:
    """ Check if a number can be divided exactly into the given number of parts.

    >>> can_be_divided(10, 2)
    True
    >>> can_be_divided(10, 3)
    False
    """