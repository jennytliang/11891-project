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

    Bracket here refers to only "(" or ")"; No [] {} or < > or whatever.

    The expression given will have an invalid "bracket pair":

    e.g., "(5 + (5 3 7"
                ^     ^ - invalid closing bracket, so add a ) right before this)
            ^                     ^--------closing of above-----------^
            opening, correct

    So this function gets passed only one of the two invalid bracket expressions:

        e.g, in "1 + 5 + (3 5 4 1", pass in '(' to
        produce the output ') + 4 1', which can then be
        prepended to

    Note:
    * This function is guaranteed to only receive one invalid opening bracket
        (the only symbol that occurs more than any other is the "(".
    * The invalid opening bracket is not necessarily immediately before the closing
          bracket; It's allowed to have a few other symbols in between.

    >>> insert_right_bracket("(4 3")
    ') 3'
    >>> insert_right_bracket(" )4")
    '( 4'
    >>> insert_right_bracket("4 8 9 4 ( + 1")
    '4 8 9 4 ) + 1'
    >>> insert_right_bracket("(2  + 3 4 - 7")
    '(2 + 3) 4 - 7'
    >>> insert_right_bracket("( + ( 3 4")
    '( + ) ( 3 4'
    """
    left = None

    for ind, char in enumerate(bracket_expr):
        if char == '(':
            left = ind     # The opening index of the problem
        elif char != '(': # It's not a left '(', but something else before the problem
            break

    # Assume the left is definitely correct, because this expression will only pass when only one bad bracket exists.
    expr = bracket_expr[left+1:]        # The part of the expr in between the two bad brackets: "(( )" --> "( )" or "(3 5"
    expr_to_return = ')' + expr[::-1]    # "( + ) 4" (reverse the string

    return left*') ' + expr_to_return
