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
        open_parens = 0
        for c in s:
            if c == '(':
                open_parens += 1
            elif c == ')':
                open_parens -= 1
            if open_parens < 0:
                return False
        return open_parens == 0

    lst = [i for i in lst if i != '']
    lst = [i for i in lst if i != ' ']
    lst = [i for i in lst if i != '']
    lst = [i for i in lst if i != ' ']
    lst = [i for i in lst if i != '']
    lst = [i for i in lst if i != ' ']
    
    for i in range(0, len(lst)):
        for j in range(0, len(lst)):
            if i != j:
                lst[i] = lst[i] + lst[j]
                if valid_parens(lst[i]) == True:
                    return 'Yes'
                lst[i] = lst[i] + lst[j]
    return 'No'


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
    def valid_par