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

    def valid_paren(string):
        open_paren = 0
        for paren in string:
            if paren == '(':
                open_paren += 1
            else:
                if open_paren == 0:
                    return False
                open_paren -= 1
        return open_paren == 0

    return 'Yes' if valid_paren(lst[0] + lst[1]) else 'No'


def match_parens_solution(lst):
    def valid_paren(string):
        open_paren = 0
        for paren in string:
            if paren == '(':
                open_paren += 1
            else:
                if open_paren == 0:
                    return False
                open_paren -= 1
        return open_paren == 0

    return 'Yes' if valid_paren(lst[0] + lst[1]) else 'No'
