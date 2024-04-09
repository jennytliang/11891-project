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
	Do not include these tokens in the code: pa
	'''



    def is_balanced(parens):
        """
        Checks if a string contains balanced parentheses
        """
        par = 0
        for p in parens:
            if p == '(':
                par += 1
            elif p == ')':
                par -= 1
            if par < 0:
                return False
        return par == 0


    if is_balanced(lst[0]) and is_balanced(lst[1]):
        return 'Yes'
    else:
        return 'No'




print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
