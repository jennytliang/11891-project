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
    # The number of opening parentheses at the beginning of the string
    n_open = 0
    # The number of opening parentheses we have counted so far
    count = 0
    # The index where the last open paren was found
    open_index = 0
    # The index where the last close paren was found
    close_index = 0
    # The index where the last space was found
    space_index = 0
    # The list of groups
    groups = []

    # Iterate over the string
    for i, c in enumerate(paren_string):
        # If we have found an open paren
        if c == '(':
            # Increment the count
            count += 1
            # If we have found the first open paren
            if count == 1:
                # Save the index
                open_index = i
            # If we have found a close paren
        elif c == ')':
            # Decrement the count
            count -= 1
            # If we have found the last close paren
            if count == 0:
                # Save the index
                close_index = i
        # If we have found a space
        elif c == ' ':
            # Save the index
            space_index = i

        # If we have found a close paren and the count is 0
        if count == 0:
            # If the space index is not the same as the close index
            if space_index != close_index:
                # Add the group to the list
                groups.append(paren_string[open_index:close_index + 1])
                # Set the open index to the space index
                open_index = space_index + 1
                # Reset the count
                count = 0

    # Add the last group to the list
    groups.append(paren_string[open_index:])

    return groups


if __name__ == '__main__':
    import doctest

    doctest.testmod()
