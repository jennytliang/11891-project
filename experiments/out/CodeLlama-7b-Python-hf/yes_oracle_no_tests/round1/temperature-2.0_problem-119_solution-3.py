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
	Do not include these tokens in the code: pass if __ name __
	'''
    def valid(string):
        """
        Checks if the string is valid
        """
        open_parens = 0
        for i in string:
            if i == '(':
                open_parens += 1
            if i == ')':
                open_parens -= 1
            if open_parens < 0:
                return False
        return open_parens == 0

    def match_parens(lst):
        """
        Checks if the list is valid
        """
        for i in range(len(lst)):
            if not valid(lst[i]):
                return 'No'
        return 'Yes'

    return match_parens(lst)
