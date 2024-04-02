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
	'''
    if not lst:
        return 'No'
    if len(lst) == 1:
        return 'Yes'
    else:
        if valid_parens(lst[0]) == 'Yes':
            if valid_parens(lst[1]) == 'Yes':
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'


def valid_parens(s):
    '''
    This is a helper function for match_parens.
    It checks if the string s is a good string.
    '''
    parens = list(s)
    if len(parens) == 0:
        return 'Yes'
    paren_count = 0
    for paren in parens:
        if paren == '(':
            paren_count += 1
        elif paren == ')':
            if paren_count > 0:
                paren_count -= 1
            else:
                return 'No'
    if paren_count == 0:
        return 'Yes'
    else:
        return 'No'
