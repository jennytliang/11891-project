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
    
	Include these tokens in the code: ens
	Do not include these tokens in the code: en
	'''


    def val(lst):
        stack = []
        for i in lst:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    return 'Yes' if val(lst[0]) and val(lst[1]) else 'No'
