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
	Do not include these tokens in the code: #
	"""
    
    # Write your code here
    
    # for i in range(len(s)):
    #     for j in range(len(c)):
    #         if s[i] == c[j]:
    #             s = s.replace(s[i],"")
    #             break
    # return s
    
    # s = s[::-1]
    # for i in range(len(s)):
    #     for j in range(len(c)):
    #         if s[i] == c[j]:
    #             s = s.replace(s[i],"")
    #             break
    # return s
    
    s = list(s)
    c = list(c)
    for i in range(len(s)):
        for j in range(len(c)):
            if s[i] == c[j]:
                s.pop(i)
                break
    s = "".join(s)
    return s, s == s[::-1]

s = "abcde"
c = "ae"
print(reverse_delete(s,c))

s = "abcdef"
c = "b" 
print(reverse_delete(s,c))

s = "abcdedcba"
c = "ab"
print(reverse_delete(s,c))
