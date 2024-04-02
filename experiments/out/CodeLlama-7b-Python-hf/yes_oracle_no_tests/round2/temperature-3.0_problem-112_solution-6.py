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
    
	Include these tokens in the code: ".
	"""

    s_list = list(s)
    for i in range(0,len(s_list)):
        for j in range(0,len(c)):
            if s_list[i] == c[j]:
                s_list[i] = ""
    s_new = ""
    for i in range(0,len(s_list)):
        s_new += s_list[i]
    if s_new == s_new[::-1]:
        return (s_new,True)
    else:
        return (s_new,False)
        

print(reverse_delete("abcde","ae"))
print(reverse_delete("abcdef","b"))
print(reverse_delete("abcdedcba","ab"))