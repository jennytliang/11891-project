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
    def valid_parens(s):
        open_parens = 0
        for char in s:
            if char == '(':
                open_parens += 1
            else:
                if open_parens <= 0:
                    return False
                open_parens -= 1
        return open_parens == 0
    
    if not valid_parens(lst[0]) or not valid_parens(lst[1]):
        return 'No'
    
    for i in range(len(lst[0])):
        for j in range(len(lst[1])):
            if valid_parens(lst[0][:i] + lst[1][j:]):
                return 'Yes'
    return 'No'
