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
    
    if nt == '':
        return True
    
    else: 
        if nt[0] == '<':
            #if ">" is in the string, the return True, because ">" is 
            #the closing bracket for any opening "<"
            if ">" in nt:
                return correct_bracketing(nt[nt.index(">"):])
            
        else:
            return False


def no_repeated(brackets:str):
    """
    brackets is a string of "(" and ")".
    return True if there aren't two repeating brackets in a row

    >>> no_repeated("(")
    True
    >>> no_repeated("()")
    True
    >>> no_repeated("(()")
    False
    >>> no_repeated(")(")
    False
    >>> no_repeated(")(")
    False
    >>> no_repeated(")())(")
    False
    """
    
    if brackets == '':
        return True
    
    elif brackets[1:2] != '(' and brackets[1:2] != ')':
        return no_repeated(brackets[1:])
    
    elif brackets[1:2] == '(':
        return no_repeated(brackets[2:])
    
    elif brackets[1:2] == ')':
        return no_repeated(brackets[2:])


def not_bracket(brackets:str):
    """
    brackets is a string of "(" and ")". 
    Return True if there is no bracket inside another bracket in the string.
    
    >>> not_bracket(')()(')
    True
    
    >>> not_bracket('(()')
    True
    
    >>> not_bracket(')()(')
    True
    
    >>> not_bracket(')()(')
    True
    
    >>> not_bracket('()()()')
    True
    """
    if brackets == '':
        return True
    
    elif brackets[0