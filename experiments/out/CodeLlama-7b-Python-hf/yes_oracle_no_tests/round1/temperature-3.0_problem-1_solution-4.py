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
    # results = []
    # cnt = 0
    # group = []
    # for char in paren_string:
    #     if char == '(':
    #         cnt += 1
    #         group.append(char)
    #     elif char == ')':
    #         cnt -= 1
    #         group.append(char)
    #     else:
    #         pass
    #     if not cnt:
    #         results.append(''.join(group))
    #         group = []
    # return results

    results = []
    group = []
    cnt = 0
    for char in paren_string:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        group.append(char)
        if not cnt:
            results.append(''.join(group))
            group = []
    return results


if __name__ == '__main__':
    import doctest

    doctest.testmod()
