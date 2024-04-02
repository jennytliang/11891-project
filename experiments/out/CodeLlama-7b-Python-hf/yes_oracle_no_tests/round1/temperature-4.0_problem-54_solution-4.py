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
	Do not include these tokens in the code: s 0 is not None and ( sorted
	"""


    
    if s0 == s1:
        return True
    else:
        if s0 == '':
            return False
        else:
            for i in range(len(s0)):
                if s0[i] in s1:
                    s1 = s1.replace(s0[i], '', 1)
                elif s1 == '':
                    return False
                else:
                    return False
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()