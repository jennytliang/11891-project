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
    
	Do not include these tokens in the code: # Set the alphabet to check for
	"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in s0:
        if char in alphabet:
            if s0.count(char) != s1.count(char):
                return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
