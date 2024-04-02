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
    group = ''
    results = []

    for char in paren_string:
        if char == '(':
            group += char
        elif char == ')':
            group += char
            results.append(group)
            group = ''
        else:
            continue

    return results


def count_paren_groups(paren_string: str) -> int:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    count those groups and return the count.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> count_paren_groups('( ) (( )) (( )( ))')
    3
    
	Include these tokens in the code: c nt , group , results =
	"""
    group = ''
    results = 0

    for char in paren_string:
        if char == '(':
            group += char
        elif char == ')':
            group += char
            results += 1
            group = ''
        else:
            continue

    return results


def count_valid_paren_groups(paren_string: str) -> int:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    count those groups that are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> count_valid_paren_groups('( ) (( )) (( )( ))')
    2
    
	Include these tokens in the code: c nt , group , results =
	"""
    group = ''
    results = 0

    for char in paren_string:
        if char == '(':
            group += char
        elif char == ')':
            group += char
            results += 1
            group = ''
        else:
            continue

    return results


def count_valid_paren_groups_recursive(paren_string: str) -> int:
   