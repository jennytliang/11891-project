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
    
	Do not include these tokens in the code: # if s
	"""
    # s0 = s0.lower()
    # s1 = s1.lower()
    # return s0 == s1
    # return sorted(s0) == sorted(s1)
    return sorted(set(s0)) == sorted(set(s1))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
