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

    def valid_paren(paren):
        stack = []
        for p in paren:
            if p == '(':
                stack.append(p)
            elif p == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack

    return 'Yes' if valid_paren(lst[0] + lst[1]) else 'No'


def test_function():
    assert match_parens(['()(', ')']) == 'Yes', 'First set'
    assert match_parens([')', ')']) == 'No', 'Second set'
    assert match_parens(['((', ')')) == 'Yes', 'Third set'
    assert match_parens(['(((', ')')']) == 'No', 'Forth set'
    assert match_parens(['((((', ')')']) == 'No', 'Fifth set'
    assert match_parens(['(((((', ')')']) == 'No', 'Fifth set'
    assert match_parens(['(((((', '))')']) == 'Yes', 'Fifth set'
    assert match_parens(['(((((', '())')']) == 'Yes', 'Fifth set'
    assert match_parens(['(((((', '((())')']) == 'Yes', 'Fifth set'
    assert match_parens(['(((((', '((())('']) == 'No', 'Fifth set'
    assert match_parens(['(((((', '((())())']) == 'No', 'Fifth set'
    assert match_parens(['(((((', '((()))())']) == 'Yes', 'Fifth set'
    assert match_parens(['(((((', '(((())())']) == 'Yes', 'Fifth set'
    assert match_parens(['(((((', '((()))())(']) == 'No', 'Fifth set'
    assert match_parens(['(((((', '(((())())(']) == 'No', 'Fifth set'
    assert match_parens(['(((((', '((()))())(']) == 'No', 'Fifth set'
    assert match_