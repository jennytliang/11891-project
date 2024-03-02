from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []

    if len(paren_string) == 1:
        return [paren_string]

    if len(paren_string) == 2:
        if paren_string[0] == '(' and paren_string[1] == ')':
            return [paren_string]
        else:
            return []

    if paren_string[0] == '(' and paren_string[1] == ')':
        return [paren_string] + separate_paren_groups(paren_string[2:])

    if paren_string[0] == '(':
        return separate_paren_groups(paren_string[1:])

    if paren_string[-1] == ')':
        return separate_paren_groups(paren_string[:-1])

    return []


if __name__ == '__main__':
    import doctest

    doctest.testmod()