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
    
	Do not include these tokens in the code: # BEGIN _ S OL UT ION
	"""
    # BEGIN _ S OL UT ION
    if s0 == s1:
        return True
    else:
        return False
    # END _ S OL UT ION

if __name__ == "__main__":
    import doctest
    doctest.testmod()