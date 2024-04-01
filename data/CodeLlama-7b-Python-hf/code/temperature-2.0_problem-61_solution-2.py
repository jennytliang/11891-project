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
    opening = 0
    for bracket in brackets:
        if bracket == "(":
            opening += 1
        elif bracket == ")":
            if opening == 0:
                return False
            else:
                opening -= 1
    return opening == 0


def correct_bracketing_stack(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_stack("(")
    False
    >>> correct_bracketing_stack("()")
    True
    >>> correct_bracketing_stack("(()())")
    True
    >>> correct_bracketing_stack(")(()")
    False
    """
    opening = []
    for bracket in brackets:
        if bracket == "(":
            opening.append(bracket)
        elif bracket == ")":
            if len(opening) == 0:
                return False
            else:
                opening.pop()
    return len(opening) == 0