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
    
	Do not include these tokens in the code: #
	"""
    # YOUR CODE HERE
    stack = []
    for b in brackets:
        if b == '<':
            stack.append('<')
        elif b == '>':
            if stack == []:
                return False
            stack.pop()
    return stack == []


def is_well_formed_bracket_string(s: str):
    """
    s is a string.
    return True if it is a properly bracketed string.
    return False otherwise.

    >>> is_well_formed_bracket_string('(())')
    True
    >>> is_well_formed_bracket_string('(()')
    False
    >>> is_well_formed_bracket_string('))')
    False
    >>> is_well_formed_bracket_string('>')
    False
    >>> is_well_formed_bracket_string('(>')
    False
    >>> is_well_formed_bracket_string('(>]')
    False
    >>> is_well_formed_bracket_string('(<>)')
    True
    >>> is_well_formed_bracket_string('(<>)<>')
    False
    """
    # YOUR CODE HERE
    stack = []
    for b in s:
        if b == '(':
            stack.append('(')
        elif b == ')':
            if stack == []:
                return False
            stack.pop()
    return stack == []


def count_correct_bracketing(strings: list):
    """ strings is a list of strings.
    return the number of strings that are properly bracketed.

    >>> count_correct_bracketing(['<', '<<>', '(())'])
    2
    >>> count_correct_bracketing(['<', '<<>', '(()']
    1
    >>> count_correct_bracketing(['<', '<<>', '))']
    0
    >>> count_correct_bracketing(['<', '<<>', '>']
    0
    """
    # YOUR CODE HERE
    count = 0
