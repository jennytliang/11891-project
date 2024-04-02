from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: nt , group , results
	"""

    # nt is a list containing the number of open and closed parentheses
    nt = [0, 0]
    # group is a list containing the string of the current group
    group = []
    # results is a list containing the final list of strings
    results = []

    for i in paren_string:
        if i == "(":
            nt[0] += 1
            group.append(i)
        elif i == ")":
            nt[1] += 1
            group.append(i)
            if nt[0] == nt[1]:
                results.append("".join(group))
                group = []
                nt = [0, 0]
        else:
            continue
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
