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
	Do not include these tokens in the code: stack = '' if lst
	'''

    def valid_parens(s):
        stack = []
        for i in s:
            if i == '(':
                stack.append('(')
            elif i == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    if lst[0][-1] == '(' and lst[1][0] == ')' and valid_parens(lst[0] + lst[1]):
        return 'Yes'
    elif lst[1][-1] == '(' and lst[0][0] == ')' and valid_parens(lst[1] + lst[0]):
        return 'Yes'
    else:
        return 'No'