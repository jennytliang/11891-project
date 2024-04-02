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
    result = []
    group = ""
    n = 0
    for char in paren_string:
        if char == "(":
            n += 1
        elif char == ")":
            n -= 1
        if n == 0:
            result.append(group)
            group = ""
        else:
            group += char
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
