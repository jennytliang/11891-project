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
    
	Do not include these tokens in the code: # the filter method removes all of
	"""
    s = s.strip()
    c = c.strip()
    if s == '':
        return (s,True)
    if c == '':
        return (s,True)
    if c == s:
        return ('',False)
    if c in s:
        s = ''.join(s.split(c))
    s = s[::-1]
    if s == s[::-1]:
        return (s,True)
    else:
        return (s,False)
