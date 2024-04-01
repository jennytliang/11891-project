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
    """
    if len(brackets) < 2:
        return False
    pairs = 0
    for char in brackets:
        if char == '(':
            pairs +=1
        elif char == ')':
            pairs -=1
            if pairs < 0: # to catch multiple close brackets before their open ones. ex) )(()) or )))(( where the first close brackets matches its open one even though its not followed by another close one. 
             return False 
    return pairs == 0 # to check that at end, not just at any point in function.


# copy-paste below code into console so that  you can see the output.
if __name__ == "__main__":
    import doctest
    print("running doctest on correct_bracketing() with code in doc string")
    doctest.testmod(exclude_empty=False)    