def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    
	Include these tokens in the code: c nt =
	"""
    # YOUR CODE HERE
    cnt=0
    for i in brackets:
        if i=="(":
            cnt+=1
        elif i==")":
            cnt-=1 
        if cnt<0:
            cnt=0
    return cnt==0
    



def other_brackets(s: str):
    """
        Return True if all brackets in the string s are properly balanced

        >>> other_brackets('(())')
        True
        >>> other_brackets('((())')
        False
    
    
    """
    """
    :s: str containing brackets
    :returns: bool

    >>> other_brackets('[({}[])](((()())))')
    True
    >>> other_brackets('[(])')
    False
    >>> other_brackets('[()')
    False
    
    """
    # YOUR CODE HERE
    check=[]
    for a in s:
        if a=="(":
            check.append(a)
        elif a==")":
            if len(check)==0 or check[-1]!="(":
                return False
            else:
                check.pop()
    if len(check)==0:
        return True
    return False

  

if __name__ == "__main__":
    import doctest
    doctest.testmod()