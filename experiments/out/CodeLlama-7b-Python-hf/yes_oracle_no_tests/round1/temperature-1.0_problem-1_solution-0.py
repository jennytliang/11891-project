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
    # separate the groups
    c = 0
    group = ""
    list_group: str = ""
    results: list = []
    for paren_char in paren_string:
        if paren_char == "(":  # count opening
            c += 1
        elif paren_char == ")":  # count closing, if balanced, break
            if c > 0:
                c -= 1
                group += paren_char
        if c == 0:
            if group:
                list_group += group
                results.append(list_group)
                list_group = ""
                group = ""
    return results

    # another solution
    # separate_paren_groups = []
    # c = 0
    # current_string = ""
    # for char in paren_string:
    #     if char == "(":
    #         current_string += char
    #         c += 1
    #     elif char == ")":
    #         current_string += char
    #         c -= 1
    #         if c == 0:
    #             separate_paren_groups.append(current_string)
    #     if c < 0:
    #         return "invalid parentheses"
    # if c > 0:
    #     return "invalid parentheses"
    # return separate_paren_groups
    # if not paren_string:
    #     return []
    # stack_open_paren = []
    # separate_paren_groups = []
    # for char in paren_string:
    #     if char == "(":
    #         stack_open_paren.append((char))
    #     elif char == ")":
    #         if stack_open_paren:
    #             separate_paren_groups.append(stack_open_paren.pop())
    #     else:
    #         print(f"invalid parentheses")
    # return separate_paren_groups
