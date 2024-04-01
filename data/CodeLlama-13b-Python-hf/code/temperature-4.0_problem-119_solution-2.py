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
    '''

    if lst == []: return 'No'

    def check(pstr):
        return not any([ not x[0] and not x[1]
                      or not x[1] and any([ not x[0] and not ch == ')' for ch in pstr[:x[1]]])
                           or not x[1] and any([ not pstr[ch-1] and not(pstr[ch]) == 1 and ch !=  x[0]
                      

