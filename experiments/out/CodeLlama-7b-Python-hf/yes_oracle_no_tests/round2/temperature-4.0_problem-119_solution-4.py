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

    def valid_parens(string):
        if string == '':
            return True
        if string[0] == ')':
            return False
        else:
            return valid_parens(string[1:])

    lst = [lst[0], lst[1]]
    lst_new = []
    for i in lst:
        lst_new.append(i[::-1])
    lst.extend(lst_new)
    for i in lst:
        if valid_parens(i):
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert match_parens(['()(', ')']) == 'Yes', "1st example"
    assert match_parens(['(())', '()']) == 'Yes', "2nd example"
    assert match_parens(['(()', ')']) == 'No', "3rd example"
    assert match_parens(['(', ')']) == 'No', "4th example"
    assert match_parens(['(()', '))']) == 'No', "5th example"
    assert match_parens([')(', ')']) == 'No', "6th example"
    assert match_parens([')(', '(']) == 'Yes', "7th example"
