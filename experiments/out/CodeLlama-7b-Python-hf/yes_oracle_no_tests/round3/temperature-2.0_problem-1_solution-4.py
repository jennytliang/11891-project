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
    # check if the string is empty, if so return an empty list
    if len(paren_string) == 0:
        return []
    # check if the string is a single parentheses, if so, return a list with one element
    if len(paren_string) == 1:
        return ["("]

    # initialize the list of groups
    groups = []
    # initialize the list of open parentheses
    open_parens = []
    # initialize a counter for the number of parentheses
    paren_count = 0
    # initialize a string to hold the current group
    current_group = ""
    # iterate through the string
    for paren in paren_string:
        if paren == "(":
            # if the paren is an open paren, increase the counter
            paren_count += 1
            # if the counter is 1, then we have a new group
            if paren_count == 1:
                # add the current group to the list of groups
                groups.append(current_group)
                # reset the current group to an empty string
                current_group = ""
            # add the current parentheses to the current group
            current_group += paren
        if paren == ")":
            # if the paren is a close paren, decrease the counter
            paren_count -= 1
            # if the counter is 0, then we have a new group
            if paren_count == 0:
                # add the current group to the list of groups
                groups.append(current_group)
                # reset the current group to an empty string
                current_group = ""
            # add the current parentheses to the current group
            current_group += paren
    # add the final group to the list of groups
    groups.append(current_group)
    # return the list of groups
    return groups


if __name__ == "__main__":
    import doctest

    doctest.testmod()
