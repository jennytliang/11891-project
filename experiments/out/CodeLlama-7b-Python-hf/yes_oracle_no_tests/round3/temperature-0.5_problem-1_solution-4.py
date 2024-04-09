from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results
	Do not include these tokens in the code: n t
	"""
    results = []
    group = ""
    n = 0
    for c in paren_string:
        if c == '(':
            n += 1
            group += c
        elif c == ')':
            n -= 1
            group += c
            if n == 0:
                results.append(group)
                group = ""
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
    
	Include these tokens in the code: c nt , group , results
	Do not include these tokens in the code: n t
	"""
    results = []
    group = ""
    nt = 0
    for c in paren_string:
        if c == '(':
            nt += 1
            group += c
        elif c == ')':
            nt -= 1
            group += c
            if nt == 0:
                results.append(group)
                group = ""
        else:
            group += c
    return results


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
