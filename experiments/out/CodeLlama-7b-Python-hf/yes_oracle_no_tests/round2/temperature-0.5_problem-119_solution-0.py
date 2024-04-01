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


    def valid_paired_parens(s):
        open_parens = 0
        for c in s:
            if c == '(':
                open_parens += 1
            elif c == ')':
                open_parens -= 1
            if open_parens < 0:
                return False
        return open_parens == 0


    def concat(s1, s2):
        s = s1 + s2
        if valid_paired_parens(s):
            return True
        return False


    s1 = lst[0]
    s2 = lst[1]
    if concat(s1, s2):
        return 'Yes'
    if concat(s2, s1):
        return 'Yes'
    return 'No'
