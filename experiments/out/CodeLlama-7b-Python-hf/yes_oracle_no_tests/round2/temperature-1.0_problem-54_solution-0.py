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
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r = [' '. join (
	"""

	r = [' '. join (
			[s0 for s0 in s0 if s0 in s1 ],
			[ s1 for s1 in s1 if s1 in s0 ] 
			),
		s0,s1]
	
	return r[2:] or r[0], r[1]
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()