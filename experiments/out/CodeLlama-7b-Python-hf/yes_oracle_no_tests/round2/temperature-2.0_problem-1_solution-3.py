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
    # 1. Start with an empty list
    # 2. Loop through the string
    # 3. If the first char is a left paren, add 1 to the counter
    # 4. If the first char is a right paren, subtract 1 from the counter
    # 5. If the counter is 0 after this, add the current string to the list
    # 6. Keep looping through the string
    # 7. Return the list

    counter = 0
    current_group = ''
    groups = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            counter += 1
            current_group += paren_string[i]
        elif paren_string[i] == ')':
            counter -= 1
            current_group += paren_string[i]
            if counter == 0:
                groups.append(current_group)
                current_group = ''
        else:
            current_group += paren_string[i]

    return groups


if __name__ == '__main__':
    import doctest

    doctest.testmod()
