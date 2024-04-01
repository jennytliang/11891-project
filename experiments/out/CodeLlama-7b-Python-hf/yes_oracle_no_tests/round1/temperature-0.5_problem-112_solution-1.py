def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
	Include these tokens in the code:  ss = " ". join ( filter (
	Do not include these tokens in the code: for i
	"""

    # s = s[::-1]
    # s = s.replace(c, "")
    # s = s[::-1]
    # if s == s[::-1]:
    #     return s, True
    # else:
    #     return s, False

    s = s[::-1]
    s = s.replace(c, "")
    s = s[::-1]
    return s, s == s[::-1]


def test_function():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("abba", "a") == ('bb', True)
    assert reverse_delete("a", "a") == ('', True)
    assert reverse_delete("aaaa", "a") == ('', True)
    assert reverse_delete("aabba", "a") == ('bb', False)
    assert reverse_delete("aaaaa", "a") == ('', True)
