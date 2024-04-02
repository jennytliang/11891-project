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
    def validate_parentheses(string):
        open_parens = 0
        for i in string:
            if i == '(':
                open_parens += 1
            elif i == ')':
                if open_parens == 0:
                    return False
                open_parens -= 1
        if open_parens == 0:
            return True
        return False
    if len(lst) == 2:
        if validate_parentheses(lst[0]) and validate_parentheses(lst[1]):
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'


if __name__ == '__main__':
    print(match_parens(['()(', ')']))
    print(match_parens([')', ')']))
