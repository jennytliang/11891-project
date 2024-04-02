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
    return len(s0) == len(s1) and set(s0) == set(s1)


def same_chars_no_set(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars_no_set('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars_no_set('abcd', 'dddddddabc')
    True
    >>> same_chars_no_set('dddddddabc', 'abcd')
    True
    >>> same_chars_no_set('eabcd', 'dddddddabc')
    False
    >>> same_chars_no_set('abcd', 'dddddddabce')
    False
    >>> same_chars_no_set('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Do not include these tokens in the code: if len ( s 0 ) !=
	"""
    return len(s0) == len(s1) and all(c in s1 for c in s0)


def main():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    main()
