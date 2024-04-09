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
    
	Include these tokens in the code: par ens
	Do not include these tokens in the code: pa ired
	'''



    def match(lst):
        if len(lst) == 0:
            return True
        if len(lst) == 1:
            return False
        if len(lst) == 2:
            return lst[0] == ')' and lst[1] == '('
        for i in range(len(lst)):
            if lst[i] == '(':
                if lst[i+1] == ')':
                    return True
                else:
                    lst.pop(i+1)
                    lst.pop(i)
                    return match(lst)
            else:
                lst.pop(i)
                return match(lst)

    return 'No' if match(lst) else 'Yes'


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
    '''
    def match(lst):
        if len(lst) == 0:
            return True
        if len(lst) == 1:
            return False
        if len(lst) == 2:
            return lst[0] == ')' and lst[1] == '('
        for i in range(len(lst)):
            if lst[i] == '(':
                if lst[i+1] == ')':
                    return True
                else:
                    lst.pop(i+1)
                    lst.pop(i)
                    return match(lst)
            else:
                lst.pop