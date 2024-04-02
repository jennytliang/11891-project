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
    # TODO: Write this function
    c = 0
    nt = 0
    group = ''
    results = []
    for i in paren_string:
        if i == '(':
            c += 1
            nt += 1
        if i == ')':
            c -= 1
            nt -= 1
        if nt == 0:
            results.append(group)
            group = ''
        if c >= 0:
            group += i
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
