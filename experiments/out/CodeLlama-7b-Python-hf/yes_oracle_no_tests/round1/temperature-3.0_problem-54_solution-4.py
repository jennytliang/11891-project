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
    # s0 = s0.lower()
    # s1 = s1.lower()
    # if len(s0) != len(s1):
    #     return False
    # for i in range(len(s0)):
    #     if s0[i] not in s1 or s1[i] not in s0:
    #         return False
    # return True

    return sorted(s0.lower()) == sorted(s1.lower())


# print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
# print(same_chars('abcd', 'dddddddabc'))
# print(same_chars('dddddddabc', 'abcd'))
# print(same_chars('eabcd', 'dddddddabc'))
# print(same_chars('abcd', 'dddddddabce'))
# print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))
