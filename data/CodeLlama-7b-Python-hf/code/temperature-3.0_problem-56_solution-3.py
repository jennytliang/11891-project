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
    # TODO: implement this function
    pass


def bracket_depth(brackets: str):
    """
    return the depth of the bracket stack
    >>> bracket_depth("()")
    1
    >>> bracket_depth("<><>")
    2
    >>> bracket_depth("<>")
    0
    >>> bracket_depth("<<>>>>")
    3

    """
