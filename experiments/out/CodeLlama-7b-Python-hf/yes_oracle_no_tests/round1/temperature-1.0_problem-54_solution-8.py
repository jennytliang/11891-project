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
	Do not include these tokens in the code: sorted
	"""

    r = ''
    for i in s0[:]:
        if i not in r:
            r += i

    for x in s1:
        if x in r:
            r += x
    return len(r) == len(s0) == len(s1)


same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
same_chars('abcd', 'dddddddabc')
same_chars('dddddddabc', 'abcd')
same_chars('eabcd', 'dddddddabc')
same_chars('abcd', 'dddddddabce')
same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
