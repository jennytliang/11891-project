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
    
	Include these tokens in the code: return set ( s
	Do not include these tokens in the code: r =
	"""
    return set(s0) == set(s1)


def same_chars_v2(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_v2('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_v2('abcd', 'dddddddabc')
    True
    >>> same_chars_v2('dddddddabc', 'abcd')
    True
    >>> same_chars_v2('eabcd', 'dddddddabc')
    False
    >>> same_chars_v2('abcd', 'dddddddabce')
    False
    >>> same_chars_v2('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: return s0 == s1
	Do not include these tokens in the code: r =
	"""
    return s0 == s1


def same_chars_v3(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_v3('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_v3('abcd', 'dddddddabc')
    True
    >>> same_chars_v3('dddddddabc', 'abcd')
    True
    >>> same_chars_v3('eabcd', 'dddddddabc')
    False
    >>> same_chars_v3('abcd', 'dddddddabce')
    False
    >>> same_chars_v3('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: return set ( s0 ) == set ( s1 )
	Do not include these tokens in the code: r =
	"""
    return set(s0) == set(s1)
