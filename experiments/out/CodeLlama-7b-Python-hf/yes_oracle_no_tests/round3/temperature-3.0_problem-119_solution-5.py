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


    def val(c):
        if c == '(':
            return 1
        return -1

    def is_balanced(s):
        res = 0
        for c in s:
            res += val(c)
            if res < 0:
                return False
        return res == 0

    def concat(s1, s2):
        return s1 + s2

    s1 = lst[0]
    s2 = lst[1]
    return 'Yes' if is_balanced(concat(s1, s2)) else 'No'
