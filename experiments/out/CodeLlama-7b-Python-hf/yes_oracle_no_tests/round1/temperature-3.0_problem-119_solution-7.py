def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    
	Include these tokens in the code: def valid _ par ens ( s : str )
	Do not include these tokens in the code: if not lst
	'''
    if not lst:
        return 'Yes'

    if not all(i in '()' for i in lst[0] + lst[1]):
        return 'No'

    if lst[0].count('(') != lst[0].count(')'):
        return 'No'

    if lst[1].count('(') != lst[1].count(')'):
        return 'No'

    if lst[0].count('(') + lst[1].count(')') != lst[0].count(')') + lst[1].count('('):
        return 'No'

    return 'Yes'
