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
    
    # s = s[::-1]
    # print(s)
    # ss = ""
    # for i in s:
    #     if i not in c:
    #         ss += i
    # print(ss)
    # if ss == ss[::-1]:
    #     return True
    # else:
    #     return False
    
    return (s[::-1], s[::-1] == s)


reverse_delete("abcde", "ae")
reverse_delete("abcdef", "b")
reverse_delete("abcdedcba", "ab")
reverse_delete("abcdefg", "abcdefg")
reverse_delete("abcdefg", "abc")
reverse_delete("abcdefg", "abcdefgabc")
reverse_delete("abcdefg", "abcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg", "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg")
reverse_delete("abcdefg",