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


    def val_parens(lst):
        ans = 0
        for elm in lst:
            if elm == '(':
                ans += 1
            else:
                ans -= 1
        return ans

    lst1 = []
    lst2 = []
    for elm in lst:
        if elm == '(':
            lst1.append(elm)
        else:
            lst2.append(elm)
    if val_parens(lst1) == 0 and val_parens(lst2) == 0:
        return 'Yes'
    elif val_parens(lst1) == 0 and val_parens(lst2) != 0:
        return 'No'
    elif val_parens(lst1) != 0 and val_parens(lst2) == 0:
        return 'No'
    elif val_parens(lst1) != 0 and val_parens(lst2) != 0:
        if val_parens(lst1) == val_parens(lst2):
            return 'Yes'
        else:
            return 'No'
