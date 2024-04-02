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

    r = set(s0)
    return len(r&set(s1))==len(s0)

def same_chars_better(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_better('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_better('abcd', 'dddddddabc')
    True
    >>> same_chars_better('dddddddabc', 'abcd')
    True
    >>> same_chars_better('eabcd', 'dddddddabc')
    False
    >>> same_chars_better('abcd', 'dddddddabce')
    False
    >>> same_chars_better('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: set
    Do not include these tokens in the code: sorted
    """

    r = {}
    for s0_val in s0:
        if not r.__contains__(s0_val):
            r[s0_val]=0
        r[s0_val]+=1

    for s1_val in s1:
        if r.__contains__(s1_val):
            r[s1_val]-=1
   
    for key in r.keys():
        if r.__getitem__(key)!=0:
            return False
        
    return True
