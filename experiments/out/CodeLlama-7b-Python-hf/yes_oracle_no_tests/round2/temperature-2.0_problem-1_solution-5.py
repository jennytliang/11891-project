from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	Do not include these tokens in the code: # Initialize an empty list to store
	"""
    c = 0  # count of open parentheses
    group = []  # list of strings, current group
    groups = []  # list of lists, all groups
    for token in paren_string:
        if token == "(":
            c += 1
            group.append(token)
        elif token == ")":
            if c == 0:
                groups.append(group)
                group = []
            else:
                group.append(token)
            c -= 1
        else:
            group.append(token)
    if group:
        groups.append(group)
    return ["".join(group) for group in groups]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
