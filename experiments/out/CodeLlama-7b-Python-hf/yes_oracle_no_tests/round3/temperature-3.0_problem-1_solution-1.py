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
    nt = []
    group = ''
    results = []

    for char in paren_string:
        if char == '(':
            c += 1
            group += char
        elif char == ')':
            c -= 1
            group += char
            if c == 0:
                results.append(group)
                group = ''
        elif c > 0:
            group += char
        else:
            continue

    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
