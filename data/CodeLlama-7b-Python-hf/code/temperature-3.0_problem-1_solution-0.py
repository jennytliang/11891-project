from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    temp_string = ''
    paren_stack = []
    for i in paren_string:
        if i == '(':
            paren_stack.append('(')
        elif i == ')':
            paren_stack.pop()
        temp_string += i
        if not paren_stack and len(temp_string) > 1:
            paren_groups.append(temp_string)
            temp_string = ''
    return paren_groups


if __name__ == '__main__':
    import doctest

    doctest.testmod()
