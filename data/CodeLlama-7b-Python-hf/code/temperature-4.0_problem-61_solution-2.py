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
    counter = 0

    for b in brackets:
        counter += 1 if b == '(' else -1

        if counter < 0:    # More close brackets than start brackets
            return False

    return counter == 0     # No leftovers

def insert_right_bracket(bracket_expr) -> str:   # 3-5
    r""" Given a math expression with an invalid bracket,
        find the matching bracket and return that
        expression wrapped with right parenthesis.
