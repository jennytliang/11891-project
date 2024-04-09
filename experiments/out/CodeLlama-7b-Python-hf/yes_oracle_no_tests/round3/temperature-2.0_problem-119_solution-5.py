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

    def valid_parens(parens):
        bal = 0
        for p in parens:
            if p == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0

    if not valid_parens(lst[0]) or not valid_parens(lst[1]):
        return 'No'
    return 'Yes'


print(match_parens(['()(', ')']))
print(match_parens([')', ')']))
print(match_parens(['((', ')']))
print(match_parens(['((', '))']))
print(match_parens(['(()', '))']))
print(match_parens(['(()', ')']))
print(match_parens(['((((', ')))))']))
print(match_parens(['((((', ')))((((((')))))))))))))']))
print(match_parens(['(((((', ')))))'])
print(match_parens(['(((((', ')))))))'])
print(match_parens(['(((((', ')))((((((')))))))))))))'])
