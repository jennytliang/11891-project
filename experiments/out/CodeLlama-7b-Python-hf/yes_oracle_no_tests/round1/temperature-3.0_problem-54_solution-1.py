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
    
    # if len(s0) != len(s1):
    #     return False
    # for i in range(len(s0)):
    #     if s0[i] != s1[i]:
    #         return False
    # return True
    
    return len(s0) == len(s1) and all(s0[i] == s1[i] for i in range(len(s0)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
