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
    print(''.join(list(paren_string)).replace(' ', ''))

    # Initial conditions
    cnt = 0
    group = ''
    results = []

    for char in list(paren_string):
        if char == '(':
            cnt += 1
            group += '('
        elif char == ')':
            cnt -= 1
            if cnt == 0:
                results.append(group + ')')
                group = ''
        else:
            group += char

    return results;


def separate_paren_groups2(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
	Separate groups are balanced (each open brace is properly closed) and not nested within each other	"""

    current = ""
    final_list = []
    
    def _parse(current, final_list, paren_string):
        if len(paren_string) == 0:
            final_list.append(current)
        if len(paren_string) > 0:
            if paren_string[0] == '(' and paren_string[:2] != '()':
                _parse(current + paren_string[0], final_list, paren_string[1:])
            if paren_string[0] == ')' and paren_string[:2] != '))':
                _parse(current + paren_string[0], final_list, paren_string[1:])
            if paren_string[0] != '(' and paren_string[:2] != '()':
                _parse(current + paren_string[0], final_list, paren_string[1:])
            if paren_string[0] != ')' and paren_string[:2] != '))':
                _parse(current + paren_string[0], final_list, paren_string[1:])
        return final_list
                
    return