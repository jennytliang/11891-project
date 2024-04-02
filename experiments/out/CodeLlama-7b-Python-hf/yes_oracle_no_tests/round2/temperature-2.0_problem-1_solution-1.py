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
    # initialize the list of paren groups
    paren_groups = []
    # initialize the current group
    current_group = ""
    # initialize the open paren count
    open_paren_count = 0
    for paren in paren_string:
        # if the character is an open paren, 
        # increment the open paren count, 
        # and add the token to the current group
        if paren == "(":
            open_paren_count += 1
            current_group += paren
        # if the character is a close paren, 
        # decrement the open paren count, 
        # and add the token to the current group
        elif paren == ")":
            open_paren_count -= 1
            current_group += paren
        # if the character is a space, 
        # ignore it
        elif paren == " ":
            pass
        # if the open paren count is 0, 
        # append the current group to the list of paren groups, 
        # and reset the current group
        elif open_paren_count == 0:
            paren_groups.append(current_group)
            current_group = ""
    return paren_groups


if __name__ == "__main__":
    import doctest

    doctest.testmod()
