from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    if paren_string == '':
        return []
    elif paren_string == '(':
        return ['(']
    elif paren_string == ')':
        return [')']
    elif paren_string == '()':
        return ['()']
    elif paren_string == '( )':
        return ['( )']
    else:
        c = paren_string[0]
        if c == '(':
            return ['('] + separate_paren_groups(paren_string[1:])
        else:
            return [')'] + separate_paren_groups(paren_string[1:])



def separate_paren_groups_recursive(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups_recursive('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    if paren_string == '':
        return []
    elif paren_string == '(':
        return ['(']
    elif paren_string == ')':
        return [')']
    elif paren_string == '()':
        return ['()']
    elif paren_string == '( )':
        return ['( )']
    else:
        c = paren_string[0]
        if c == '(':
            return ['('] + separate_paren_groups_recursive(paren_string[1:])
        else:
            return [')'] + separate_paren_groups_recursive(paren_string[1:])




