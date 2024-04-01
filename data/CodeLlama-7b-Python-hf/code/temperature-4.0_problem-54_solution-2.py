def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """

    return s0 is not None and (
        sorted(s0, key=lambda c: c) == sorted(s1, key=lambda c: c)
    )


def same_chars_sort(s0: str, s1: str):
    """
    Check of two words have the same characters.
    >>> same_chars_sort('eabcdzzzz', 'abdddddabcddedd')
    True
    """
    return s0 is not None and sorted(s0) == sorted(s1)


# Alternate version that uses set differencing to compare the two strings:
#   >>> same_chars('aabc', 'bcba')
#   True


def same_chars_no_sets(s0: str, s1: str):
    for c0 in s0:
        if c0 not in s1:
            return False
        else:
            idx = s1.find(c0)
            s0 = s0[idx + 1 :]
            s1 = s1[: idx + 1]

    return s0 == ''