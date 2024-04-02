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
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n _ open
	"""
    return n_open(brackets)==0
    
def n_open(brackets):
    """returns the number of opening brackets in brackets
    """
    if len(brackets)==0:
        return 0
    elif brackets[0]=="<":
        return n_open(brackets[1:])+1
    else:
        return n_open(brackets[1:])
    
    
def n_close(brackets):
    """returns the number of closing brackets in brackets
    """
    if len(brackets)==0:
        return 0
    elif brackets[0]==">":
        return n_close(brackets[1:])+1
    else:
        return n_close(brackets[1:])
    
def n_open_close(brackets):
    """returns the number of opening and closing brackets in brackets
    """
    if len(brackets)==0:
        return 0
    elif brackets[0]=="<":
        return n_open_close(brackets[1:])+1
    elif brackets[0]==">":
        return n_open_close(brackets[1:])-1
    else:
        return n_open_close(brackets[1:])
    
    
def correct_bracketing_iter(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing_iter("<")
    False
    >>> correct_bracketing_iter("<>")
    True
    >>> correct_bracketing_iter("<<><>>")
    True
    >>> correct_bracketing_iter("><<>")
    False
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: n _ open
	"""
    if len(brackets)==0:
        return True
    elif brackets[0]=="<":
        return correct_bracketing_iter(brackets[1:])
    elif brackets[0]==">":
        return