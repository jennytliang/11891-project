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
    # first reverse the string s
    s_reverse = s[::-1]
    # create an empty string
    s_new = ""
    # iterate through the string s
    for i in range(len(s)):
        # check if the character in s is not in c
        if s[i] not in c:
            # if the character is not in c, add it to s_new
            s_new += s[i]
    # check if the reversed s_new is equal to s
    if s_new == s_reverse:
        # if it is, return True
        return (s_new, True)
    # otherwise return False
    return (s_new, False)


if __name__ == '__main__':
    s = "abcde"
    c = "ae"
    print(reverse_delete(s,c))
    s = "abcdef"
    c = "b"
    print(reverse_delete(s,c))
    s = "abcdedcba"
    c = "ab"
    print(reverse_delete(s,c))
