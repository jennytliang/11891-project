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
    
	Include these tokens in the code: ". join ( filter ( lambda
	"""

    sList = list ( s )


    for i in range ( len ( sList ) ):
        if sList [ i ] in c:
            sList.remove ( sList [ i ] )


    s_list = ''.join ( sList )


    if len ( s_list ) <= 1:
        return

    else:
        while s_list [ - 1 : -2 : -1 ] != s_list [ 0 : len ( s_list ) - 2 ]:
            sList.pop ( -1 )
            s_list = ''.join ( sList )
            if len ( s_list ) <= 1:
                return

        return ''.join ( s_list ), True






