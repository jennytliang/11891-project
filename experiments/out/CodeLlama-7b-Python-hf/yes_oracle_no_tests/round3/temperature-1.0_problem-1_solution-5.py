from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group ,
	Do not include these tokens in the code: # results : List [ str ]
	"""
    # results: List[str] = []
    # group: str = ''
    # c: int = 0
    # nt: int = 0
    # for i in paren_string:
    #     if i == '(':
    #         nt += 1
    #     if i == ')':
    #         nt -= 1
    #     if i == ' ':
    #         continue
    #     if nt == 0:
    #         results.append(group)
    #         group = ''
    #     group += i
    # results.append(group)
    # return results
    return [i for i in paren_string.replace(' ', '').split('(') if i]


def get_first_and_last_paren_group(paren_string: str) -> str:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the first and last group.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> get_first_and_last_paren_group('( ) (( )) (( )( ))')
    '()'
    """
    # group: str = ''
    # c: int = 0
    # nt: int = 0
    # for i in paren_string:
    #     if i == '(':
    #         nt += 1
    #     if i == ')':
    #         nt -= 1
    #     if i == ' ':
    #         continue
    #     if nt == 0:
    #         return group
    #     group += i
    # return group
    return paren_string.replace(' ', '').split('(')[0] + paren_string.replace(' ', '').split('(')[-1]


def get_nth_paren_group(paren_string: str, n: int) -> str:
    """ Input to this function is a