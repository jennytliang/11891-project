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
    # c is the number of open parentheses
    # nt is the number of parentheses that are not yet closed
    c = 0
    nt = 0
    group = ""
    results = []

    for char in paren_string:
        if char == "(":
            c += 1
            nt += 1
        elif char == ")":
            if nt == 0:
                raise ValueError("Parentheses are unbalanced")
            nt -= 1
            if nt == 0:
                results.append(group)
                group = ""
        else:
            group += char

    if nt != 0:
        raise ValueError("Parentheses are unbalanced")
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
