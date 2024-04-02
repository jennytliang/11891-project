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
    group = []
    groups = []
    open_count = 0
    close_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
            group.append(char)
        elif char == ')':
            close_count += 1
            group.append(char)
            if open_count == close_count:
                groups.append(''.join(group))
                group.clear()
                open_count = 0
                close_count = 0
        else:
            continue
    return groups


def separate_paren_groups_2(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    group = []
    groups = []
    open_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
            group.append(char)
        elif char == ')':
            open_count -= 1
            group.append(char)
            if open_count == 0:
                groups.append(''.join(group))
                group.clear()
        else:
            continue
    return groups


if __name__ == "__main__":
    import doctest

    doctest.testmod()
