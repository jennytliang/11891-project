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
    
	Do not include these tokens in the code: r = [] for
	"""
    return sorted(s0) == sorted(s1)


def same_chars_no_loops(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_no_loops('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_no_loops('abcd', 'dddddddabc')
    True
    >>> same_chars_no_loops('dddddddabc', 'abcd')
    True
    >>> same_chars_no_loops('eabcd', 'dddddddabc')
    False
    >>> same_chars_no_loops('abcd', 'dddddddabce')
    False
    >>> same_chars_no_loops('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)


def same_chars_no_loops_no_sort(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_no_loops_no_sort('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_no_loops_no_sort('abcd', 'dddddddabc')
    True
    >>> same_chars_no_loops_no_sort('dddddddabc', 'abcd')
    True
    >>> same_chars_no_loops_no_sort('eabcd', 'dddddddabc')
    False
    >>> same_chars_no_loops_no_sort('abcd', 'dddddddabce')
    False
    >>> same_chars_no_loops_no_sort('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    s0 = s0.replace(' ', '')
    s1 = s1.replace