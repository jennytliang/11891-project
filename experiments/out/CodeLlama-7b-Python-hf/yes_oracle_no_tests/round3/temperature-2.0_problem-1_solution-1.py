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
    # Initialize the results list
    results = []
    # Initialize the group string
    group = ""
    # Initialize the count of nested parentheses
    count = 0
    # Iterate through the characters in the paren_string
    for char in paren_string:
        # If the character is an open parenthesis, increment the count
        if char == "(":
            count += 1
        # If the character is a close parenthesis, decrement the count
        if char == ")":
            count -= 1
        # If the count is zero, we are at the end of a group
        if count == 0:
            # Add the group to the results list
            results.append(group)
            # Reset the group string
            group = ""
        # Add the character to the group string
        group += char
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
