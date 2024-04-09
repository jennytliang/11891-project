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
    
	Include these tokens in the code: _ par ens
	'''

    def  _parens(lst):
        lst = [x for x in lst if x != ' ']
        # print(lst)
        if len(lst) == 0:
            return True
        if len(lst) == 1:
            return False
        if len(lst) == 2:
            if lst[0] == '(' and lst[1] == ')':
                return True
            else:
                return False
        if lst[0] == '(':
            return _parens(lst[1:])
        if lst[0] == ')':
            return _parens(lst[1:])

    return 'Yes' if _parens(lst) else 'No'


def match_parens2(lst):
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
    
	Include these tokens in the code: _ par ens
	'''

    def  _parens(lst):
        lst = [x for x in lst if x != ' ']
        # print(lst)
        if len(lst) == 0:
            return True
        if len(lst) == 1:
            return False
        if len(lst) == 2:
            if lst[0] == '(' and lst[1] == ')':
                return True
            else:
                return False
        if lst[0] == '(':
            return _parens(lst[1:])
        if lst[0] == ')