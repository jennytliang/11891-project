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
    d = {')': '(', '(': ')'}
    stack = []
    for c in lst[0] + lst[1]:
        if c in d.values():
            stack.append(c)
        elif c in d.keys():
            if stack and stack[-1] == d[c]:
                stack.pop()
            else:
                return 'No'
    return 'Yes' if not stack else 'No'
