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
    rev=s[::-1]
    rev=list(rev)
    for i in c:
        if i in s:
            for j in range(s.count(i)):
                s=s.replace(i,"")
                rev=list(s[::-1])
                if s==rev:
                    return s,True
                else:
                    return s,False
        else:
            return s,False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_delete(u"abcdxbcdy", u"y") == ('abcddcdx', True), "First Test"
    assert reverse_delete(u"abcddxbcdy", u"y") == ('abcddxbcd', False), "Second Test"
    assert reverse_delete(u"abcddxbxcdy", u"y") == ('abcddxbxcd', True), "Third Test"
    assert reverse_delete(u"abcddxbxbxcdy", u"y") == ('abcddxbxbxcd', True), "Fourth Test"
