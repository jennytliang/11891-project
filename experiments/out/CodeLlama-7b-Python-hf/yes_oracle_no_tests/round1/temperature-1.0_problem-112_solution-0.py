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

    """
    for x in s:
        if x not in c:
            ss += x
    s = ss
    if s == s[::-1]: #palindrome
      return (s,True)
    else:
      return (s,False)
    """
  #  def reverse_delete(s,c):
      
        # ss = ""
        # for x in s:
            # if x not in c:
                # ss += x
        # return (ss,ss == ss[::-1])

    ss = ""
    for x in s:
        if x not in c:
            ss += x
    s = ss
    if s == s[::-1]: #palindrome
        return (s,True)    
    else:
        return (s,False)
