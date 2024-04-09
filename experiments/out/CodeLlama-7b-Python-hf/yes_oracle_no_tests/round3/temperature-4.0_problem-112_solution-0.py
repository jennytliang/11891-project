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
	Do not include these tokens in the code: # s
	"""
    #code goes here
    return ss, ss == ss[::-1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_delete('abcde', 'ae') == ('bcd', False), "First"
    assert reverse_delete('abcdef', 'b') == ('acdef', False), "Second"
    assert reverse_delete('abcdedcba', 'ab') == ('cdedc', True), "Third"
    assert reverse_delete('abc', 'abc') == ('', True), "Four"
    assert reverse_delete('abcba', 'ab') == ('c', True), "Fifth"
    print('"Run" is good. How is "Check"?')
