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
	Do not include these tokens in the code: s
	"""
    rev = s[::-1]
    rev = list(rev)
    for i in range(len(rev)):
        if rev[i] in c:
            rev[i] = ''
    rev = ''.join(rev)
    rev = list(rev)
    if rev == rev[::-1]:
        return (rev, True)
    else:
        return (rev, False)
    
reverse_delete("abcde", "ae")