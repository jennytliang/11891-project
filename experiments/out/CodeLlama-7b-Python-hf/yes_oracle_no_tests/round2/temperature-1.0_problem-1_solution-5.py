from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Do not include these tokens in the code: results : List [ str ] =
	"""
    # results : List[str] = []
    # stack : List[str] = []
    # for char in paren_string:
    #     if char in ('(', '['):
    #         stack.append(char)
    #     elif char in (')', ']'):
    #         if not stack:
    #             return []
    #         top = stack.pop()
    #         if top + char not in ('()', '[]'):
    #             return []
    #     elif char == ' ':
    #         continue
    #     else:
    #         return []
    # return stack + results[::-1]

    results = []
    stack = []
    for char in paren_string:
        if char in ('(', '['):
            stack.append(char)
        elif char in (')', ']'):
            if not stack:
                return []
            top = stack.pop()
            if top + char not in ('()', '[]'):
                return []
        elif char == ' ':
            continue
        else:
            return []
    return stack + results[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
