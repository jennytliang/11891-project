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
    
	Do not include these tokens in the code: if len ( s 0 ) !=
	"""
    return sorted(s0) == sorted(s1)


def same_chars_set(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_set('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_set('abcd', 'dddddddabc')
    True
    >>> same_chars_set('dddddddabc', 'abcd')
    True
    >>> same_chars_set('eabcd', 'dddddddabc')
    False
    >>> same_chars_set('abcd', 'dddddddabce')
    False
    >>> same_chars_set('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Do not include these tokens in the code: if len ( s 0 ) !=
    """
    return len(set(s0)) == len(set(s1))


def same_chars_dict(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_dict('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_dict('abcd', 'dddddddabc')
    True
    >>> same_chars_dict('dddddddabc', 'abcd')
    True
    >>> same_chars_dict('eabcd', 'dddddddabc')
    False
    >>> same_chars_dict('abcd', 'dddddddabce')
    False
    >>> same_chars_dict('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Do not include these tokens in the code: if len ( s 0 ) !=
    """
    return len([value for key, value in dict.fromkeys(s0).items()]) == len(
        [value for key, value in dict.fromkeys(s1).items()]