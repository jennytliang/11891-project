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
    results = []
    group = ''
    cnt = 0
    for i in paren_string:
        if i == '(':              # Count brace
            cnt += 1
            group += i
        elif i == ')' and cnt == 0 and group == '':   # if its an incorrect bracket
            return None
        elif i == ')' and cnt == 1:          # if it is a valid closing brace
            cnt -= 1
            group += i
        elif i == ')' and cnt != 1:          # if its a nested brace
            group += i

        if group != '' and cnt == 0:         # If entire bracket is formed and we reached 0 then reset
            results.append(group)
            group = ''
    return results
