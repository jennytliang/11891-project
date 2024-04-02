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
    
	Do not include these tokens in the code: # s = s [
	"""
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in c:
            s_list[i] = ''
    s_list = ''.join(s_list)
    if s_list == s_list[::-1]:
        return (s_list, True)
    else:
        return (s_list, False)
