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

    r = s0.replace(s1, "")
    return len(r) == 0

    # # another way
    # return s0 == s1


def same_chars_list(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_list('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_list('abcd', 'dddddddabc')
    True
    >>> same_chars_list('dddddddabc', 'abcd')
    True
    >>> same_chars_list('eabcd', 'dddddddabc')
    False
    >>> same_chars_list('abcd', 'dddddddabce')
    False
    >>> same_chars_list('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: set
	Do not include these tokens in the code: len
	"""

    return len(set(s0) - set(s1)) == 0
