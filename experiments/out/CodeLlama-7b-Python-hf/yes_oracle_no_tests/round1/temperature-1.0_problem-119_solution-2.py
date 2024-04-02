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
    l1 = []
    l2 = []
    for i in lst[0]:
        if i == '(':
            l1.append(i)
        elif i == ')':
            if l1:
                l1.pop()
            else:
                l2.append(i)
    for i in lst[1]:
        if i == '(':
            l2.append(i)
        elif i == ')':
            if l2:
                l2.pop()
            else:
                l1.append(i)
    if l1 == [] and l2 == []:
        return 'Yes'
    else:
        return 'No'


def test_match_parens():
    assert match_parens(['()(', ')']) == 'Yes'
    assert match_parens([')', ')']) == 'No'
