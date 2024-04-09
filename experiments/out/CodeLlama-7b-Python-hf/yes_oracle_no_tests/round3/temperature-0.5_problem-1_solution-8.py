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
    # c is a counter of open parens
    # nt is a flag for nesting
    # group is the current group
    # results is the final list of results
    c = 0
    nt = False
    group = ""
    results = []
    for char in paren_string:
        if char == "(":
            c += 1
            nt = True
        elif char == ")":
            c -= 1
            if c == 0:
                results.append(group)
                group = ""
                nt = False
            else:
                group += ")"
        if nt:
            group += char
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
