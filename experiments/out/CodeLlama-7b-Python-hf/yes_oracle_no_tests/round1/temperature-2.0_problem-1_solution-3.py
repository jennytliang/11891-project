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
    c = 0
    for i in paren_string:
        if i == '(':
            c += 1
            group += i
        elif i == ')':
            c -= 1
            group += i
            if c == 0:
                results.append(group)
                group = ''
                c = 0
        elif i == ' ':
            continue

    return results


if __name__ == '__main__':
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) (( )) (( ) ( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('( ) (( )) (( ) ( )( )) ( )') == ['()', '(())', '(()())']
