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
	'''
    def valid_parens(s):
        open_parens = 0
        for char in s:
            if char == '(':
                open_parens += 1
            elif char == ')':
                open_parens -= 1
            if open_parens < 0:
                return False
        return open_parens == 0

    def match_parens(lst):
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                s = lst[i] + lst[j]
                if valid_parens(s):
                    return 'Yes'
        return 'No'

    return match_parens(['()(', ')'])


print(match_parens(['()(', ')']))
