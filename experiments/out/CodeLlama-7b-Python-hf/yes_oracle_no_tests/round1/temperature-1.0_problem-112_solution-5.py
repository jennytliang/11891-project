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
    res = ""
    for i in s :
        if i not in c:
            res += i
    #print(f"res= {res}")
    if res[::-1] ==res:
        print(True)
    else :
        print(False)
    return (res, True if res[::-1] ==res else False)

    # print(f"({res}, {True if res[::-1] ==res else False})")

reverse_delete("abcde", "ae")
reverse_delete("abcdef", "b") 
reverse_delete("abcdedcba", "ab")
