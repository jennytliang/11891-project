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
    assert s0.isalpha()
    assert s1.isalpha()
    assert len(s0) > 0
    assert len(s1) > 0

    for char in s0:
        if char not in s1:
            return False
    for char in s1:
        if char not in s0:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
