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
    """ 
    To find the groups, we can loop over the string, incrementing a counter for each "(" and decrementing one for each ")".
    When we reach 0, we know we have found a new group.
    To keep track of open and closed brackets, we can keep using a counter (or the built-in enumerate function).
    We add one to the group count each time we see a "(" and subtract one every time we see a "(".
    Then after the entire string has been scanned, we can divide the number of groups by 2 to get the number of brackets.
    We can get the number of open brackets using

    >> [group for (group, open_count) in zip(reversed(range(N)), open_counts) if open_count != 0]
    
    Then we can just split the string at those indices. 
    """
    groups = 0
    counter = 0
    open_counts = []
    indices = [0]

    for i, bracket in enumerate(paren_string):

        if bracket == "(":
            counter += 1
            open_counts.append(counter)
        elif bracket == ")":
            counter -= 1
            open_counts.append(counter)
        else:
            raise ValueError("A bad parenthesis entered {0} at position {1}".format(bracket, i))

        if counter == 0:
            groups += 1
            indices.append(i)

    return [paren_string[i:j] for (i, j) in zip(indices, indices[1:] + [None])]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
