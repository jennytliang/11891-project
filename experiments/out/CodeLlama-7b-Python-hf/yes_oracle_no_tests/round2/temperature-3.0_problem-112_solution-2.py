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
    
	Include these tokens in the code: ss
	Do not include these tokens in the code: s = list ( s )
	"""
    #code goes here
    s = s[::-1]
    for i in c:
        s = s.replace(i, "")
    s = s[::-1]
    return s, s[::-1] == s
    
if __name__ == '__main__':
    print("Example:")
    print(reverse_delete('abcde', 'ae'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_delete('abcde', 'ae') == ('bcd', False)
    assert reverse_delete('abcdef', 'b') == ('acdef', False)
    assert reverse_delete('abcdedcba', 'ab') == ('cdedc', True)
    assert reverse_delete('abba', 'ab') == ('', True)
    assert reverse_delete('a', 'a') == ('', True)
    assert reverse_delete('aabbc', 'xyz') == ('aabbc', True)
    print("Coding complete? Click 'Check' to earn cool rewards!")
