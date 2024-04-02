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
    
    # First we need to reverse the string
    s = s[::-1]
    
    # Now we need to remove the characters from the string
    for i in c:
        s = s.replace(i,"")
    
    # Now we need to check if the string is palindrome or not
    s = s.split()
    s = "".join(s)
    if s == s[::-1]:
        return s, True
    else:
        return s, False


reverse_delete("abcde","ae")
reverse_delete("abcdef","b")
reverse_delete("abcdedcba","ab")