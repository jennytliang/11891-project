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
	Do not include these tokens in the code: len
	"""

    r = set(s0) & set(s1)
    return len(r) == len(s0) == len(s1)


def same_chars_faster(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_faster('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_faster('abcd', 'dddddddabc')
    True
    >>> same_chars_faster('dddddddabc', 'abcd')
    True
    >>> same_chars_faster('eabcd', 'dddddddabc')
    False
    >>> same_chars_faster('abcd', 'dddddddabce')
    False
    >>> same_chars_faster('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: set
	Do not include these tokens in the code: len
	"""

    r = set(s0) & set(s1)
    return len(s0) == len(s1) and len(r) == len(s0)


def same_chars_fasterer(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_fasterer('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_fasterer('abcd', 'dddddddabc')
    True
    >>> same_chars_fasterer('dddddddabc', 'abcd')
    True
    >>> same_chars_fasterer('eabcd', 'dddddddabc')
    False
    >>> same_chars_fasterer('abcd', 'dddddddabce')
    False
    >>> same_chars_fasterer('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
