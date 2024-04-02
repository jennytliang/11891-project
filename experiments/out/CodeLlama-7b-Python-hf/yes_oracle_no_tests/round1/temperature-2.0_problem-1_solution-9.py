from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results =
	"""
    results = []
    group = ''
    n_open = 0
    n_close = 0
    for c in paren_string:
        if c == '(':
            if n_open > 0:
                group += c
            n_open += 1
        elif c == ')':
            if n_close > 0:
                group += c
            n_close += 1
        if n_open == n_close and n_open > 0:
            results.append(group)
            group = ''
            n_open = 0
            n_close = 0
        else:
            group += c
    return results


def separate_paren_groups_v2(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results =
	"""
    results = []
    group = ''
    n_open = 0
    for c in paren_string:
        if c == '(':
            n_open += 1
        elif c == ')':
            n_open -= 1
        if n_open == 0:
            results.append(group)
            group = ''
        else:
            group += c
    return results


def separate_paren_groups_v3(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input