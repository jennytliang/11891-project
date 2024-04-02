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
    # Initialize an empty list to store results
    results = []
    # Initialize a counter to keep track of the parentheses
    c = 0
    # Initialize a string to store the current group
    group = ""
    # Loop through the string
    for char in paren_string:
        # If the character is an open bracket, add one to the counter
        if char == "(":
            c += 1
        # If the character is a close bracket, subtract one from the counter
        elif char == ")":
            c -= 1
        # If the counter is zero, then the group is complete
        if c == 0:
            # Add the group to the results list
            results.append(group)
            # Reset the group
            group = ""
        # No matter what, add the character to the group
        group += char
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
