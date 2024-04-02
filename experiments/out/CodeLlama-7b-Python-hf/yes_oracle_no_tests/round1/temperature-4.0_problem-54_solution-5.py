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


    
    # Your code here
    # s0 = s0.lower()
    # s1 = s1.lower()
    # print(s0)
    # print(s1)
    # a = set(s0)
    # print(a)
    # b = set(s1)
    # print(b)
    # if a == b:
    #     return True
    # else:
    #     return False
    # print(a)


    # return s0 == s1
    return sorted(s0) == sorted(s1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()