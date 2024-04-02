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
    r = list(s)
    w = []
    for s in r:
        for c in c:
            if s==c:
                r.pop(s)
                w.pop(s)
    r = ''.join(map(str,r))
    if reverse_delete(r,r):
        if reverse_delete(r,r)==True:
            return r, True
        else:
            return r, False

print(reverse_delete("abcde","ae"))