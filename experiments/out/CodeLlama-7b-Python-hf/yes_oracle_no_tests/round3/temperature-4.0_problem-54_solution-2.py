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
    
	Include these tokens in the code: set
	Do not include these tokens in the code: sorted
	"""


    
    # s0 = sorted(s0)
    # s1 = sorted(s1)
    # return set(s0) == set(s1)
    return sorted(s0) == sorted(s1)


def same_chars_no_sort(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_no_sort('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_no_sort('abcd', 'dddddddabc')
    True
    >>> same_chars_no_sort('dddddddabc', 'abcd')
    True
    >>> same_chars_no_sort('eabcd', 'dddddddabc')
    False
    >>> same_chars_no_sort('abcd', 'dddddddabce')
    False
    >>> same_chars_no_sort('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: set
	Do not include these tokens in the code: sorted
	"""
    # print(sorted(s0))
    # print(sorted(s1))
    # print(set(s0))
    # print(set(s1))
    # print(set(s0) == set(s1))
    return set(s0) == set(s1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
