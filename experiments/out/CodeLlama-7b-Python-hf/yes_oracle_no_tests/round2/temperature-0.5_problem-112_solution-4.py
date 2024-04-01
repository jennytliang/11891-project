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
    l = list(s)
    for i in range(len(l)):
        if l[i] in c:
            l[i] = ""
    s = "".join(l)
    if s == s[::-1]:
        return (s,True)
    else:
        return (s,False)

if __name__ == '__main__':
    print(reverse_delete("abcde", "ae"))
    print(reverse_delete("abcdef", "b"))
    print(reverse_delete("abcdedcba", "ab"))
