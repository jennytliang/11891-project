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
    # the filter method removes all of the characters in c from s
    # the join method adds a space between each character
    ss = " ".join(filter(lambda ch: ch not in c, s))
    return ss, ss == ss[::-1]

def reverse_delete2(s,c):
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
    # the filter method removes all of the characters in c from s
    # the join method adds a space between each character
    ss = " ".join(filter(lambda ch: ch not in c, s))
    return ss, ss == ss[::-1]

    
if __name__=="__main__":
    print(reverse_delete("abcde", "ae"))
    print(reverse_delete("abcdef", "b"))
    print(reverse_delete("abcdedcba", "ab"))
    print(reverse_delete2("abcde", "ae"))
    print(reverse_delete2("abcdef", "b"))
    print(reverse_delete2("abcdedcba", "ab"))