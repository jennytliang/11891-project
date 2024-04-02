from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	"""
    if paren_string == "":
        return []
    groups = []
    group = ""
    open_parens_counter = 0
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            open_parens_counter += 1
            group += "("
        elif paren_string[i] == ")":
            open_parens_counter -= 1
            group += ")"
        if open_parens_counter == 0:
            groups.append(group)
            group = ""

    return groups


if __name__ == "__main__":
    import doctest

    doctest.testmod()
