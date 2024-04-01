from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string or len(paren_string) == 0:
        return []

    if len(paren_string) == 1:
        return [paren_string]

    if len(paren_string) == 2:
        if paren_string[0] == '(' and paren_string[1] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 3:
        if paren_string[0] == '(' and paren_string[2] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 4:
        if paren_string[0] == '(' and paren_string[3] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 5:
        if paren_string[0] == '(' and paren_string[4] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 6:
        if paren_string[0] == '(' and paren_string[5] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 7:
        if paren_string[0] == '(' and paren_string[6] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 8:
        if paren_string[0] == '(' and paren_string[7] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 9:
        if paren_string[0] == '(' and paren_string[8] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 10:
        if paren_string[0] == '(' and paren_string[9] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 11:
        if paren_string[0] == '(' and paren_string[10] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 12:
        if paren_string[0] == '(' and paren_string[11] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 13:
        if paren_string[0] == '(' and paren_string[12] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 14:
        if paren_string[0] == '(' and paren_string[13] == ')':
            return [paren_string]
        else:
            return []

    if len(paren_string) == 15:
        if paren_string[0] == '(' and paren_string[14] == ')':
            return [paren_string]
        else:
            return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
