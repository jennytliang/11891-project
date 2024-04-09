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
    # initialize the list to store the separated groups
    results = []
    
    # initialize the counter for the number of parentheses
    cnt = 0
    
    # initialize the string to store the group
    group = ''
    
    for char in paren_string:
        if char == '(':
            cnt += 1
            group += char
        elif char == ')':
            cnt -= 1
            group += char
        if cnt == 0:
            results.append(group)
            group = ''
    
    return results


if __name__ == '__main__':
    import doctest
    doctest.testmod()
