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
    # Write your code here.
    output_list = []
    group_string = ''
    paren_stack = []
    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
            group_string += char
        elif char == ')':
            paren_stack.pop()
            group_string += char
            if len(paren_stack) == 0:
                output_list.append(group_string)
                group_string = ''
        if char == ' ':
            continue

    return output_list


if __name__ == '__main__':
    import doctest

    doctest.testmod()
