from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # 1 . Start with an
	"""
    if not paren_string or paren_string[0] != "(":
        return []
    paren_stack = []
    paren_group_start = 0
    paren_group_list = []
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            paren_stack.append("(")
            if len(paren_stack) == 1:
                paren_group_start = i
        if paren_string[i] == ")":
            if len(paren_stack) > 0:
                paren_stack.pop()
                if len(paren_stack) == 0:
                    paren_group_list.append(paren_string[paren_group_start : i + 1])
    return paren_group_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
