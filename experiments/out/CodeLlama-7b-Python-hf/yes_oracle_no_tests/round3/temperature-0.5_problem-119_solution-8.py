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
    return 'Yes' if check_parens(lst[0] + lst[1]) else 'No'

def check_parens(s):
    if s == '':
        return True
    if s[0] == ')' or s[-1] == '(':
        return False
    return check_parens(s[1:]) and check_parens(s[:-1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert match_parens(['()(', ')']) == 'Yes', "1st example"
    assert match_parens(['((', ')']) == 'No', "2nd example"
    assert match_parens(['()', '()']) == 'Yes', "3rd example"
    assert match_parens([')(', ')']) == 'No', "4th example"
    assert match_parens(['(', ')']) == 'Yes', "5th example"
    assert match_parens(['(', '(']) == 'Yes', "6th example"
    assert match_parens([')', ')']) == 'No', "7th example"
