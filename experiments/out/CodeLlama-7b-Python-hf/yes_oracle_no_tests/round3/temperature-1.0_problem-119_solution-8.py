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
    
	Include these tokens in the code: : str ) -> bool :
	Do not include these tokens in the code: ):
	'''


    def valid_pa(pa):
        if len(pa) % 2 == 0:
            return False
        else:
            return pa.count('(') == pa.count(')')

    def match_parens_helper(lst):
        if not lst:
            return True
        if len(lst) == 1:
            return False
        if valid_pa(lst[0]):
            return match_parens_helper(lst[1:])
        else:
            return match_parens_helper(lst[1:]) or match_parens_helper(lst[2:])

    return 'Yes' if match_parens_helper(lst) else 'No'
