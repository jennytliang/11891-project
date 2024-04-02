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
    for char in paren_string:
        if char == "(":
            nt += 1
        elif char == ")":
            nt -= 1
        group += char
        if nt == 0:
            results.append(group)
            group = ""
    return results


if __name__ == "__main__":
    print(separate_paren_groups("( ) (( )) (( )( ))"))
