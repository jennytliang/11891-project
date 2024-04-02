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

    def valid_paren(paren):
        stack = []
        for p in paren:
            if p == '(':
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        return len(stack) == 0

    if not valid_paren(lst[0]) or not valid_paren(lst[1]):
        return 'No'

    if len(lst[0]) > len(lst[1]):
        return 'No'

    for i in range(len(lst[0])+1):
        if valid_paren(lst[0][:i] + lst[1]):
            return 'Yes'

    return 'No'


# match_parens(['()(', ')']) == 'Yes'
# match_parens([')', ')']) == 'No'
print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
