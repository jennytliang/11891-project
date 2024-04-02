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
    
	Include these tokens in the code: ss = " ". join ( filter ( lambda ch
	"""
    
    # 1: reverse s
    s = s[::-1]
    
    # 2: delete the characters in s that are equal to any character in c
    for c in c:
        s = s.replace(c,"")
    
    # 3: check if the result string is palindrome
    s_rev = s[::-1]
    if s == s_rev:
        return s, True
    else:
        return s, False
    

































































































