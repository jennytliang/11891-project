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
	Do not include these tokens in the code: s = list ( s )
	"""
    # s = list ( s )
    # for i in range ( 0 , len ( s ) ) :
    #     for j in range ( 0 , len ( c ) ) :
    #         if s[i] == c[j] :
    #             del s[i]
    #             break
    # s = ''.join ( s )
    # ss = s[::-1]
    # if s == ss :
    #     return ( s , True )
    # else :
    #     return ( s , False )
    s = list ( s )
    for i in range ( 0 , len ( s ) ) :
        for j in range ( 0 , len ( c ) ) :
            if s[i] == c[j] :
                s.pop ( i )
                break
    s = ''.join ( s )
    ss = s[::-1]
    if s == ss :
        return ( s , True )
    else :
        return ( s , False )

if __name__ == '__main__':
    print(reverse_delete("abcde", "ae"))
