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
    # Please add code here
    # open_count = 0
    # close_count = 0
    # for i in lst:
    #     if i == '(':
    #         open_count += 1
    #     elif i == ')':
    #         close_count += 1
    # if open_count == close_count:
    #     return 'Yes'
    # return 'No'

    stack = []
    for i in lst:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return 'No'
    if stack:
        return 'No'
    return 'Yes'


# TESTS
tests = [
    [('()(', ')'), 'Yes'],
    [(')', ')'), 'No'],
    [('((', ')'), 'No'],
    [('(((', ')'), 'No'],
    [('(()', '))))'), 'Yes'],
    [('((())', ')'))', 'Yes'],
    [('((((', ')))))))'), 'No'],
    [('((((', ')))))))', 'No'],
    [('((((', ')))))))', 'No'],
    [('((((', ')))))))', 'No'],
    [('((((', ')))))))', 'No'],
]
for lst, expected in tests:
    actual = match_parens(lst)
    print('match_parens({}) -> {} == {}'.format(lst, actual, expected))
    assert actual == expected
