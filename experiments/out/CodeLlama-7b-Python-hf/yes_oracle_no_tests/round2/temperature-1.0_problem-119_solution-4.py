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
    
	Do not include these tokens in the code: # open = [' ( ',' [
	'''
    def match_parens_helper(lst):
        if len(lst) == 0:
            return True
        if len(lst) == 1:
            if lst[0] == '(':
                return False
            else:
                return True
        if len(lst) == 2:
            if lst[0] == '(' and lst[1] == ')':
                return True
            elif lst[0] == ')' and lst[1] == '(':
                return False
            else:
                return True
        if len(lst) >= 3:
            if lst[0] == '(' and lst[1] == ')':
                return match_parens_helper(lst[2:])
            elif lst[0] == ')' and lst[1] == '(':
                return match_parens_helper(lst[2:])
            elif lst[0] == '(' and lst[2] == ')':
                return match_parens_helper(lst[1:])
            elif lst[0] == ')' and lst[2] == '(':
                return match_parens_helper(lst[1:])
            elif lst[1] == '(' and lst[2] == ')':
                return match_parens_helper(lst[0:2])
            elif lst[1] == ')' and lst[2] == '(':
                return match_parens_helper(lst[0:2])
            else:
                return match_parens_helper(lst[1:])
    if match_parens_helper(lst[0]) and match_parens_helper(lst[1]):
        return 'Yes'
    else:
        return 'No'


def match_parens2(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example