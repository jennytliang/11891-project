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
	Do not include these tokens in the code: # Your code here open
	'''
    open_parens = lst[0]
    close_parens = lst[1]
    open_count = 0
    close_count = 0
    for i in open_parens:
        if i == '(':
            open_count += 1
    for j in close_parens:
        if j == ')':
            close_count += 1
    if open_count == close_count:
        return 'Yes'
    return 'No'


print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
print(match_parens(['(())', ')()']) == 'Yes')
print(match_parens(['(())(', ')()']) == 'Yes')
print(match_parens(['())', ')']) == 'No')
print(match_parens(['(())', ')']) == 'No')
print(match_parens(['()', '()']) == 'Yes')
print(match_parens(['()', '(())']) == 'Yes')
print(match_parens(['()', '(()']) == 'No')
print(match_parens(['()', '(()']) == 'No')
print(match_parens(['()', '(())']) == 'Yes')
print(match_parens(['()', '(())']))
