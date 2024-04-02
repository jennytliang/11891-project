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
	Do not include these tokens in the code: for i
	"""
    c = str(c)
    i = []
    for c_i in c: 
        i.append(c_i)
    j = []
    for _ in s: 
        j.append(_)
    for i in xrange(len(i)):
        while i in j: 
            j.remove(i)
    k= ""
    for _ in j: 
        k += _
    for k_i in xrange(len(k)):
        if k[k_i] == k[k_i+(k_i*(-1))]:
            return (k, True)
        else: 
            return (k, False)