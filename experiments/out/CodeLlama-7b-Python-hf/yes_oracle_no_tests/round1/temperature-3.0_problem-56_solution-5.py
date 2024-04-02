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
    
	Include these tokens in the code: c nt =
	"""
    # c = 0
    # nt = 0
    # for i in brackets:
    #     if i == '<':
    #         c += 1
    #     if i == '>':
    #         nt += 1
    # if c == nt:
    #     return True
    # else:
    #     return False

    # return (len(brackets) - brackets.count('>') == brackets.count('<'))
    # return (len(brackets) - brackets.count('>') == brackets.count('<'))
    return (brackets.count('>') == brackets.count('<'))


def first_correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return the first correct bracketing of the string,
    or None if there is no such bracketing.

    >>> first_correct_bracketing('><')
    '><'
    >>> first_correct_bracketing('')
    >>> first_correct_bracketing('<>')
    '<>'
    >>> first_correct_bracketing('>>')
    >>> first_correct_bracketing('<<<>>>')
    '<><><>'
    >>> first_correct_bracketing('<<><>>')
    '<><><>'
    >>> first_correct_bracketing('><<>')
    >>> first_correct_bracketing('<><<>>')
    '<><><>'
    """
    # if len(brackets) == 0:
    #     return None
    # if correct_bracketing(brackets):
    #     return brackets
    # for i in range(len(brackets)):
    #     if correct_bracketing(brackets[:i] + brackets[i+1:]):
    #         return brackets[:i] + brackets[i+1:]
    # return None
    # if correct_bracketing(brackets):
    #     return brackets
    # for i in range(len(brackets)):
    #     if correct_bracketing(brackets[:i] + brackets[i+