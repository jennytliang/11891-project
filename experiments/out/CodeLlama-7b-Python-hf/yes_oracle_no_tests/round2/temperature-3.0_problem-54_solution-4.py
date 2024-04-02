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
    
	Include these tokens in the code: return set
	Do not include these tokens in the code: # s 0 = s 0 .
	"""
    # s0 = s0.lower()
    # s1 = s1.lower()
    return set(s0) == set(s1)
    
#print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
#print(same_chars('abcd', 'dddddddabc'))
#print(same_chars('dddddddabc', 'abcd'))
#print(same_chars('eabcd', 'dddddddabc'))
#print(same_chars('abcd', 'dddddddabce'))
#print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))

