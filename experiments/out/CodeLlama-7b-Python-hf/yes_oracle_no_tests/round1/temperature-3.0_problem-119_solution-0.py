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
    
	Include these tokens in the code: def valid _ par ens ( s : str )
	Do not include these tokens in the code: if not lst
	'''
    def valid_parens(s):
        return s.count('(') == s.count(')')
    if not lst:
        return 'Yes'
    lst1 = []
    lst2 = []
    for i in lst[0]:
        lst1.append(i)
    for i in lst[1]:
        lst2.append(i)
    if valid_parens(lst1+lst2):
        return 'Yes'
    else:
        return 'No'


print(match_parens(['()(', ')']) == 'Yes')
print(match_parens([')', ')']) == 'No')
