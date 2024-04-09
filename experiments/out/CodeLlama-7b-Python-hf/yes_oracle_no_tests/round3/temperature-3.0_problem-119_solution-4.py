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
    
	Include these tokens in the code: s : str ) -> bool :
	Do not include these tokens in the code: par ens ):
	'''


    def valid_pairs(lst):
        pairs = []
        for i in lst:
            if i == ')':
                if pairs[-1] == '(':
                    pairs.pop()
                else:
                    return False
            else:
                pairs.append(i)
        return True


    return 'Yes' if valid_pairs(lst[0]) and valid_pairs(lst[1]) else 'No'
