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
    
	Include these tokens in the code: valid _ par ens
	Do not include these tokens in the code: bal anced
	'''


 
    def is_balanced(string):
        if string == '':
            return True
        if string[0] == '(' and string[-1] == ')':
            return is_balanced(string[1:-1])
        else:
            return False

    return 'Yes' if is_balanced(lst[0] + lst[1]) else 'No'
