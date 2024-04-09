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
    
	Include these tokens in the code: s : str ) -> bool :
	Do not include these tokens in the code: par en ):
	'''


    def valid_pairs(lst):
        if len(lst) == 0:
            return True
        if len(lst) == 1:
            return False
        if len(lst) == 2:
            return lst[0] == '(' and lst[1] == ')'
        return lst[0] == '(' and lst[2] == ')' and valid_pairs(lst[1:])

    return 'Yes' if valid_pairs(lst) else 'No'


# EOF
