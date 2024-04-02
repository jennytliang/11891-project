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
	Do not include these tokens in the code: result = "" chars =
	"""
    #First we delete all the chars in c from s 
    ss = ""
    for i in range(0, len(s)):
        if s[i] not in c:
            ss += s[i]
    #Then we check reversely
    reverse = ss[::-1]
    if reverse == ss:
        return [ss, True]
    return [ss, False]   

reverse_delete("abcde","ae") # returns: ['bcd', False]
reverse_delete("abcdef","b") # returns: ['acdef', False]
reverse_delete("abcdedcba","ab") # returns: ['cdedc', True]