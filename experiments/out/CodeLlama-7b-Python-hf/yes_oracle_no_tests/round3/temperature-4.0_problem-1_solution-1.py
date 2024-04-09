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
    # c = current position
    # n = next position
    # t = token
    c = 0
    n = 1
    group = []
    results = []

    while c < len(paren_string):
        t = paren_string[c]
        if t == "(":
            group.append(t)
        elif t == ")":
            group.append(t)
            results.append("".join(group))
            group = []
        c += 1

    return results


if __name__ == "__main__":
    print(separate_paren_groups("( ) (( )) (( )( ))"))
    print(separate_paren_groups("((()))((()))"))
