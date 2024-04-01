def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """

    # print(stack)
    brackets_stack = brackets.split('><')
    # if we reach the last one,  we have only 0 or 4, both of those return True

    return brackets.count('>') == brackets.count('<')

    ### another possibility

