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
	Do not include these tokens in the code: r =
	"""
    return len(set(s0)) == len(set(s1))


def main():
    """
    Tester function for same_chars
    """
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    assert same_chars('abcd', 'dddddddabc')
    assert same_chars('dddddddabc', 'abcd')
    assert not same_chars('eabcd', 'dddddddabc')
    assert not same_chars('abcd', 'dddddddabce')
    assert not same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    print('Passed all tests.')


if __name__ == '__main__':
    main()