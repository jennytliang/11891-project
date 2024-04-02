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
    # initialize lists, counters and string
    string = paren_string.replace(' ', '')
    results: list = []
    group = ''
    open_count, closed_count = 0, 0

    for character in string:
        if character == '(':
            open_count += 1
            group = '('
        # if it's not left paren, we need to make sure if it's right paren, then count and close group
        elif character == ')':
            closed_count += 1
            group += character
            # now check if this is right paren of outer most group
            if closed_count == open_count:
                # if so, just add that group to results
                results.append(group)
                closed_count = 0
                open_count = 0
                group = ''
        # else if its other char, just add it to string
        else:
            group += character
    # just want to return the outer most groups so no need to return the rest
    return results


if __name__ == "__main__":
    print(separate_paren_groups('( ) (( )) (( ) ( ))'))
