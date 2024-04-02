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
    c = 0
    nt = 0
    group = ''
    results = []
    for x in paren_string:
        if x == '(': c += 1
        elif x == ')': c -= 1
        if c == 0 and nt == 0:
            results.append(group)
            group = ''
        else: group += x
        if c < 0: c = 0
    if group: results.append(group)
    return results


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
