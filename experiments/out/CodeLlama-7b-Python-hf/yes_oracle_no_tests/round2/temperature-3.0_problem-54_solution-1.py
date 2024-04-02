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
    
	Do not include these tokens in the code: # if len ( s
	"""

    # return len(s0) == len(s1) and set(s0) == set(s1)
    return s0.count(s1) == len(s1)


# print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
# print(same_chars('abcd', 'dddddddabc'))
# print(same_chars('dddddddabc', 'abcd'))
# print(same_chars('eabcd', 'dddddddabc'))
# print(same_chars('abcd', 'dddddddabce'))
# print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))
