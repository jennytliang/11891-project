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

    nt = 0
    group = ""
    results = []

    for letter in paren_string:

        if letter == "(":
            nt += 1
            group += letter
        elif letter == ")":
            if nt == 0:
                results.append(group)
                group = ""
            else:
                nt -= 1
                group += letter
        else:
            group += letter

    return results


def separate_paren_groups_2(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups_2('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: nt , group , results
	"""

    nt = 0
    group = ""
    results = []

    for letter in paren_string:

        if letter == "(":
            nt += 1
            group += letter
        elif letter == ")":
            if nt == 0:
                results.append(group)
                group = ""
            else:
                nt -= 1
                group += letter
        else:
            group += letter

    return results
