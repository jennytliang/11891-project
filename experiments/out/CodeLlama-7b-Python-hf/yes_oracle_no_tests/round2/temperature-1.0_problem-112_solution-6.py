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
    # First reverse the string
    s = s[::-1]
    # For each character in the c string, delete it from the reversed string
    for ch in c:
        s = s.replace(ch, "")
    # Reverse the string again
    s = s[::-1]
    # Check if the result is a palindrome
    if s == s[::-1]:
        return (s, True)
    else:
        return (s, False)
