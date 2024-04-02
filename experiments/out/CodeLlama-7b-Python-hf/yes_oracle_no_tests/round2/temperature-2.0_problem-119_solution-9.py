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
    
	Include these tokens in the code: def valid _ par ens
	Do not include these tokens in the code: if len
	'''
    def valid_parens(string):
        return string.count('(') == string.count(')')
    
    # First, we'll sort the list in place.
    lst.sort()
    # Then, we'll iterate through the list.
    for i in range(len(lst)):
        # If the string is not valid, return 'No'.
        if not valid_parens(lst[i]):
            return 'No'
        # If the string is valid, and the string is not the last in the list,
        # and the string is not the first in the list, check if the string is
        # valid.
        # If the string is valid, and the string is the last in the list,
        # and the string is not the first in the list, check if the string is
        # valid.
        # If the string is valid, and the string is the last in the list, and
        # the string is the first in the list, check if the string is valid.
        # If the string is valid, and the string is the first in the list, and
        # the string is not the last in the list, check if the string is valid.
        # If the string is valid, and the string is the first in the list, and
        # the string is the last in the list, check if the string is valid.
    return 'Yes'


print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
print(match_parens(['()', '()']) == 'Yes')
print(match_parens(['()', ')']) == 'No')
print(match_parens(['(', ')']) == 'Yes')
print(match_parens(['(', '()']) == 'Yes')
print(match_parens(['()', '(']) == 'Yes')
print(match_parens(['()', '()()']) == 'Yes')
print(match_parens(['()()', '()']) == 'Yes')
print(match_parens(['()()', '()()']) == 'Yes')
print(match_parens(['()', '()', '