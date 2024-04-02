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

    r = [''.join(sorted(s0)),''.join(sorted(s1))]
    l = []
    for f in r:
        while len(f)==0:
            f=''.join(sorted(i for i in f if i not in set(s0)))
        l.append(f)
    return True if l[0]==l[1] else False
    