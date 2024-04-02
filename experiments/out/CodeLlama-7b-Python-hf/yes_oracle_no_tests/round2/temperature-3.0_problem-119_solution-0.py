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
    
	Include these tokens in the code: : str ) -> bool : c nt
	Do not include these tokens in the code: ):
	'''

    def valid_parens(parens):
        balance = 0
        for p in parens:
            if p == '(':
                balance += 1
            elif p == ')':
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    def concat_parens(lst):
        if len(lst) == 1:
            return lst[0]
        else:
            return lst[0] + concat_parens(lst[1:])

    return 'Yes' if valid_parens(concat_parens(lst)) else 'No'


print(match_parens(['()(', ')']))
print(match_parens([')', ')']))
print(match_parens(['((', ')']))
print(match_parens(['((', ')', ')']))
print(match_parens(['((', ')', ')', ')']))
print(match_parens(['((', ')', ')', ')', ')']))
print(match_parens(['((', ')', ')', ')', ')', ')']))
