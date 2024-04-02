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
    # first reverse the string
    rev = s[::-1]
    # reverse delete
    for i in c:
        rev = rev.replace(i,"")
    # check if palindrome
    if rev == rev[::-1]:
        return rev,True
    else:
        return rev,False


if __name__=="__main__":
    test_data = [
        ("abcde", "ae", 'bcd', False),
        ("abcdef", "b", "acdef", False),
        ("abcdedcba", "ab", "cdedc", True),
    ]
    for s,c,result,is_palindrome in test_data:
        print("Reverse Delete:",reverse_delete(s,c))
        print("Reverse Delete:",reverse_delete(s,c) == (result,is_palindrome))
