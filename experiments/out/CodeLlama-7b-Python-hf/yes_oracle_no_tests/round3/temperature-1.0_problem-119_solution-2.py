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
    
	Include these tokens in the code: def valid
	Do not include these tokens in the code: lst
	'''
    def valid(lst):
        stack = []
        for i in lst:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if not stack:
                    return 'No'
                stack.pop()
            else:
                return 'Yes'
        if stack:
            return 'No'
        return 'Yes'
    return valid(lst)


def match_parens_2(lst):
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
    
	Include these tokens in the code: def valid
	Do not include these tokens in the code: lst
	'''
    def valid(lst):
        stack = []
        for i in lst:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if not stack:
                    return 'No'
                stack.pop()
            else:
                return 'Yes'
        if stack:
            return 'No'
        return 'Yes'
    return valid(lst)


print(match_parens(['()(', ')']))
print(match_parens(['()', '()']) == 'Yes')
print(match_parens(['(', ')']) == 'Yes')
print(match_parens(['(())', ')']) == 'Yes')
print(match_parens(['(())', '()']) == 'Yes')
print(match_parens(['(())', '(()']) == 'No')