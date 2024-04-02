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
    cnt = 0
    group = []
    result = []
    for char in paren_string:
        if char == '(':
            cnt += 1
            group.append(char)
        elif char == ')':
            cnt -= 1
            group.append(char)
            if cnt == 0:
                result.append(''.join(group))
                group = []
        elif char == ' ':
            continue
        else:
            raise ValueError('Invalid paren string')
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
