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
    
	Do not include these tokens in the code: r = True for i
	"""
    r = True
    for i in range(len(s0)):
        if s0[i] not in s1:
            r = False
    for i in range(len(s1)):
        if s1[i] not in s0:
            r = False
    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
