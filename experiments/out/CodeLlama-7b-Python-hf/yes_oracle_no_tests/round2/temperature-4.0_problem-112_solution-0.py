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
    # s = s.replace(c, '')
    return " ".join(filter(lambda ch: ch != c, s)), s == s[::-1]


if __name__ == '__main__':
    print(reverse_delete("abcde", "ae"))
    print(reverse_delete("abcdef", "b"))
    print(reverse_delete("abcdedcba", "ab"))
