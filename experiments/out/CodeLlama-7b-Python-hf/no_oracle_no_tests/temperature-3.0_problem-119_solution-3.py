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
    if not lst:
        return "Yes"
    elif len(lst) == 1:
        if lst[0] == '(':
            return "No"
        else:
            return "Yes"
    else:
        a = lst[0]
        b = lst[1]
        newlst = lst[2:]
    if a == '(' and b == ')':
        return match_parens(newlst)
    elif a == ')' and b == '(':
        return "No"
    else:
        return match_parens(lst[1:])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing




import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[['()(', ')']], [[')', ')']], [['(()(())', '())())']], [[')())', '(()()(']], [['(())))', '(()())((']], [['()', '())']], [['(()(', '()))()']], [['((((', '((())']], [[')(()', '(()(']], [[')(', ')(']], [['(', ')']], [[')', '(']], [['(', '(']], [['))', '))']], [['(', '()())(']], [['()()', '()()()']], [['(())', ')()(']], [['()()', '))']], [['((', '))']], [['(((', ')))']], [['()', ')()(']], [['())(', '()']], [['(', '((']], [['()()()()', '))']], [['()()()(', '))']], [['()()()(()())', '))']], [['', '(']], [['()()(()()()()()', '))']], [['()()()(', ')()()()(()()))']], [[')()()()(', ')()()()(()()))']], [[')()(', ')()(']], [[')()(', ')())()()()(']], [[')()()()(()()))', '(']], [['()(()()()(()()))()(()())', '))']], [['((', '(']], [['()(()()()(()()))()(()())', '()(()(()()(()()))()(()())']], [['())(', '((']], [['()()', '()()()()()()()']], [['())))(', '((']], [['', '((']], [['(((', '(']], [['()(()()()()))()(()())', '))']], [['())(', '())']], [['()()', '()()']], [['((', '((']], [[')()(', ')()))()()()(']], [['(())(', '()']], [['()()()(', '))())']], [['))())', '((']], [['', '']], [['(', '()(']], [['()())((((', ')))']], [['((', ')()(']], [['()(()()()(()()))()(()())', '()(()(()()(()()())(()())']], [['((', '()())(']], [['(())(((', '))']], [['(((', ')']], [['()()()()()()()', '']], [['()()((', ')()(']], [['((', ')()))()()()(']], [['((', '']], [['(())', ')))()))(']], [['()()(())())', '))())']], [['()()()()()()()()()()()', '()()()()()()()']], [['())))(', ')()()()(()()))']], [[')()()()(()()))', '((']], [['()())(())(', '((']], [['()()()(()())', ')()()()())']], [['((', '()()()()(()()))(']], [['())(', '())(']], [['((((', '(']], [['(())', '()())()))()()((']], [['()())((((', '))))']], [['', '()()(()()()()()']], [['()()()((', '))())']], [['()())(())(', ')()()()(()()))']], [[')()()()(()()))', '())))(']], [['', '()']], [[')()))()))))()()(', ')()))()()()(']], [[')()(', ')()()()(()()))']], [['()(()()()()))()(()())', ')()()()())']], [['())(', ')()']], [['((', '()()(']], [[')()))()))))()()(', ')()))()(()((())(']], [['(())(', '()())(())((()']], [['(()(', '()']], [['(())(((', '()()()()()()()()()()()']], [['()()()()()()()', '))))']], [['()()()((', '))(']], [['', '())']], [[')())()()()(', '()']], [['()', '()']], [['((', '()()()()()()()()()(']], [['((((', ')()))()))))()()(']], [['(())(', '()()()()()()()()())(())((()']], [['((', '()())()))()()((']], [['()())(()))(', ')()()()(()()))']], [['()(((', '()()((']], [[')()(', ')()))()()(()(']], [[')()))()()(()((((', '(']], [['())()()()()(', '()']], [['()()()(', ')()))()()(()((((']], [['()()()))))((', '))(']], [['()(()()()()))()(()())', '((']], [['()()((', '()()(']], [['(())', '(((']], [['(()(()()(()()())', ')))()))(']], [['()(()()()(()()))()(()())', '((((']], [['(((', '()()(']], [['()()()()(()()))(', '(()))(((']], [['())))(', '(']], [['(', '()(()))()']], [['(((((((', '((((())))))))']], [['()(((', '))))']], [[')(()()', '((((((())))']], [['())()()(', ')))))(']], [['(((())))', '()']], [[')()()(', '(()))']], [[')))))', '(((((']], [['((', ')))))(((']], [['(()(', '))))']], [['())()()(', ')))(()()))(']], [['(((())))', '(((())))']], [['())()()(', ')))))(((']], [[')()())(', '(()))']], [['(((())))', '(()))']], [['())()())))))(', ')))(()()))(']], [['((((())))))))', '))))']], [['()(((', ')))))']], [['((((())))))))', '((((()))))((((()))))))))))']], [['(', ')))))(((']], [['((()(', '))))']], [['((((())))))))', '((((()))))(())']], [['(', ')))))']], [['((((())))))))', '((((()))))((((())))))))))))))((())']], [[')))(()()))(', ')))(()()))(']], [['((((((())))', '))))']], [[')))(', ')))(()())))(']], [['((()((', '))))']], [['((((())))))))', '((((()))))((((()))))))))))))))((())']], [['(((())))))))((()', '(((())))']], [['((((((())())', '))))']], [[')))))(((', '())()()(']], [['()(((', '((((()))))(())']], [['((((())))))))', '((((()))))(()))(()())))()))))))))))((())']], [['(()(', ')))(()()))(']], [['(((((', '()']], [[')()()(', '(']], [['()(((', '((((())))))))))(())']], [['((((()((((((()))))))', '))))']], [['((((()(()))))))', ')))))']], [[')()(((', '((((()))))(())']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', '))))']], [['(((()()))', '(((())))']], [['((((()))))(((((())))))))))))))((())', '((((()))))((((())))))))))))))((())']], [['((((()))))(((((())))))))))))))((())', '()(()))()']], [['()', '(((())))']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', ')))(()())))(']], [[')))))(((', '))))']], [['(()()()()(', '(()))']], [[')))(()()))(((((()))))(((((())))))))))))))((())', ')))(()())))(']], [['(()))))(', '))))']], [[')((((()((((((()))))))))))', '(((((']], [['())()()(', '())()()(']], [['(', '()((((()((()']], [['((((()))))', '((((()))))((((()))))))))))))))((())']], [['(((((((', '(']], [['())()()(', '(()(']], [['()((()))(', '((((()))))(())']], [['())()())))))(', '()()))(']], [[')()(', '(()))']], [['(()(', '))))()(((']], [['()((()))(())()()(', '(()(']], [['(((((((', '((']], [['(()(', '((']], [['()(((', '()(((']], [['((', '()((((()((()']], [[')))))', '((()(()()((']], [['((((((()()))((((((()((((((()))))))(())))', '((((((()()))(((())))']], [['())()()))))', '()()))(']], [['()((()))(', '(((((((']], [[')))(((())))()))(', ')))(()()))(']], [['(((((((', '((((()))))(())']], [[')()(', '()']], [[')(()()', ')))))(((']], [['(()(', ')))))']], [['((()((()))()()()()(', '(()))']], [[')))))', ')))))']], [[')()(((', ')))(()()))(']], [['(()((', ')))(()()))(']], [['((((((())))', ')))))']], [['())()()))))', '((((())))))))']], [['())()()))(()()))()(', ')))))(((']], [['))))', '((((()))))((((()))))))))))))))((())']], [[')))))', '()((()))(']], [['(()((', ')()())(']], [['(()(', '(()))']], [[')(()()', ')(()()']], [[')))))((', ')))))(((']], [[')()())(', '()((()))(())()()(']], [[')))(()())))(', '))))']], [['((((()))))((((())))))))))))))((())', '(()))']], [[')))))', '))))']], [[')))))((', '(()))))(']], [['((((())))))))', '']], [['())()())))()())())', '((((())))))))']], [['))))', '((((()))))(())']], [['(((((', '((((()))))(())']], [['((()((()))()()()()(', '()((((()((()']], [[')()(', '(())))']], [['((()((', ')))(()()))(']], [['()(((', '()((((((())))))))))(())(']], [['()((()))(', '(((((((()))))(((((())))))))))))))((())((((']], [['()(()))()', '))))']], [[')))))', '((((()((((((()))))))']], [['((((()))))(())', '((((()))))(())']], [['()))))()(((', '()(((']], [['()(((', ')()(((']], [['())(()()(', '(()(']], [[')))))', '))(()))))))']], [['((((()))))', '(()))']], [[')()(', '((()(']], [['()((()))(', '((((()()))((((((']], [['()()))(', '()']], [['(()(', '(((']], [[')))))((', '()()))(']], [['()))(((())))()))((()(()()((', '((()(()()((']], [['(()(((((()((((((()))))))', '(()(']], [['))(()))))))', '))(()))))))']], [['()))()())))))(', '())()())))))(']], [['()((((', '()((((((())))))))))(())(']], [['((((((', '()']], [['()))()())))))(', '()(((']], [[')))))', '()(((']], [['((((()))))))))))(())', '())()())))))(']], [['())()()))))', '))))']], [[')))(', '(()((']], [['(((((((())))', ')))))']], [['((((()((((((()))))))', '))())))))()((()']], [['(((((', ')()']], [[')))))(((', '())()()))(()()))()(']], [['())()()))))', '((((()))))((((()))))))))))))))((())']], [['()(((', '(())))']], [[')()(', '((())(']], [['()))))()(((', ')))(()()))(']], [['())()())))(((()())))', '))))']], [[')))))((', '))))))(((']], [['()(((', ')((((()))']], [[')()()(', ')))(()()))(']], [['))))', '())()())))))(']], [['))))', '())()()))))']], [['((((((()()))((((((()((((((()))))))(())))', '((((((()())(((((((()))))(((())))']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', '((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))']], [[')()()(', ')()()(']], [[')))(()())))(', '()(()))()']], [['((()((', ')))))(((']], [['))))', ')))))']], [['((((()((((((()))))))', ')))))']], [['())()()))))', '((((()))))((((()))))))))))))))((()())()()))(()()))()(']], [['((((((())())', ')))))(']], [['()))))()(((', '))()((((()((())))']], [['(((((((', '(((((((']], [['()()))(', '()()))(']], [['())()()(', '((((()))))((((()))))))))))))))((())']], [['(((((((', '((((()))))(()))))((())']], [['()(((', '((()(']], [['((((()))))(((((())))))))))))))((())', '((()((()))()()()()(']], [[')()()', '((((((())))']], [['()(((', ')((((()']], [['()((()))(', '((((()())()((((((']], [['((((())))))))', '((((()))))(()))(()())))())))))))()(()))())))((())']], [['()))))()(((', ')))(((())))()))(']], [['()))()())))))(', '(()((((((())))))))))(())()(((']], [['((((()))))(())', '(()((()))))(())']], [[')))(((((()))))())(', ')))(()()))(']], [['((((((()()))((((((()((((((()))))))(())))', '((((((()())(((((((())))((((()))))))))))(())((())))']], [['()))()())))))(', '()))(((((()))))())((((']], [['())()()))(()()))()(', '((((((()())(((((((()))))(((())))']], [['(((((()))))((((()))))))))))))))((())', '(((((()))))((((()))))))))))))))((())']], [['()(()))()', '(()))))']], [['()((()))(', '(((((((((((((())))']], [['()(((())))))))', '((((())))))))']], [[')))))(((', ')))))(((']], [['()))()())))))(', '()))()())))))(']], [['((()(()(((()()((', '((()(()()((']], [['((((()))))(()))(()())))())))))))()(()))())))((())()))()())))))(', '()(((']], [['()((()))(', '((((())))']], [[')()(((', '((((((((((()))))(((((())))))))))))))((())(((((()))))(())']], [['()(((((()))))((((())))))))))))))((())((', ')()(((']], [[')((((()', ')((((()']], [[')()(', '()((((()))))((((()))))))))))']], [['((((((', '(((((']], [['))))', '(()(']], [['())()()(', '((((()((((((()))))))']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', ')))(()())))((((((((']], [[')))(()())))(', ')))((()((()))()()()()()']], [['))(()))))((((()))))(()))(()())))())))))))()(()))())))((())()))()())))))())', '))(()))))))']], [[')))(()()))))((((((((', ')))(()()))(']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', '((((((((()))))(())(((()))))))']], [['((()(', '(()))']], [['())()())())))(', ')))(()()))(']], [['()))(((())))()))((()(()()((', ')))))']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', ')))(()())))(((((((((']], [['((', '(((']], [['(()))))(', '))(((((((())))']], [['(()(((((()(((((((()))))))', '(()(']], [[')))(()()))((((())((())', ')))(()())))(']], [['))()(', '(()))']], [[')))))', '(()(']], [[')()())()())))(((()())))(((', '((((()))))(())']], [['((((()()))((((((', '()(()))()']], [['((((())))))))', '((((())))))))']], [['()(((', '((((())))))))))((()(((((()((((((()))))))())']], [['((((((())))', ')))(()())))(']], [['()()))', '()()))(']], [['((((((())))', '))']], [['((((((()())(((((((())))((((()))))))))))(())((())))', '((((()))))((((()))))))))))))))((())']], [['())()()(', '((((()(((((((()))))))']], [['))))', '((()((']], [[')))())))))()((()((((()', ')((((()']], [['((((()()))((((((', '((((()))))((((())))))))))))))((())']], [['(()((((((())))))))))(())()(((', '())()()(']], [['(())))', '(())))']], [[')()()(', ')))))']], [['())))()())))))(', '()))()())))))(']], [['((((((((()))()))))))', ')))(()())))((((((((']], [['()))()(', ')))))(((']], [[')()((((', '((((()))))(())']], [['()((())))))))((', '(((((((()))))((((((())))))))))))))((())((((']], [['())()()))))', '))()((((()((())))']], [['()))()(', ')((((()']], [['()(((((())))', '((((()(((((((()))))))((((((())))']], [[')()()(', ')()(((']], [['())()())))(((()())))', '())()())))(((()())))']], [['())()()))))', ')((((()))))(((((()())))))(']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((((()()))(((())))((((()))))))', '(()((((((())))))))))(())()(((']], [['))(()))))((((()))))(()))(()())))())))))))()(()))())))((()))()))()())))))())', '))(())))))()']], [[')))(()()))))(((((((()(()()', '((((((())))']], [['()((((((())))))))))(())(', '((((()()))((((((']], [['(()))))(', '))(()))))((((()))))(()))(()())))())))))))()(()))())))((()))()))()())))))())']], [[')(()()', '((((())))))))']], [['((()(((()))()()()()(', '(()))']], [['())()()))))', ')((((()))))(((((()())))(']], [['((()((', '']], [[')))))))))))(((()(())', '())()())))))(']], [['()(((()))(', '((((()())()((((((']], [['))()(((', '))()(((']], [['((()(((()))()()()()())()()(', '(()))']], [['()(((()))(', '(((((()())(()((((((']], [['(()(', '((((()))))(()))(()())))())))))))()(()))())))((())']], [['())()()))))', '((((()))))(((((()()()()(()))))))))))))))((())']], [['))(()))))))', '((((()(((((((()))))))((((((())))']], [['()(((((()))))((((())))))))))))))((())((', ')()((']], [['))))))(((', '))))))(((']], [['())()()))))', ')))(()())))(']], [['()()))', '(((((()))))(()))))((()))()))(']], [['((((()))))(()))(()())))())))))))))(()))))))()(()))())))((())()))()())))))(', '()(((']], [[')()(', '(((((()))))))))))(())())))']], [['((((()((((((())))))))', '))))']], [['((((((((()))))(()))((()())))()))))))))))((())()((((((()))))))', '((((((((()))))(()))(()())))()))))))))))((())()((((((())(())))))))']], [['())())()))))', '())()()))))']], [['((((((()()))(((())))', '((((((()))()']], [['()(((', ')(()((()']], [['((((()))))(())', '(()((())()))(())']], [['((', '()(()))()']], [['()', '(((()))))(()()))())']], [['((()(', ')))))']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((((()()))(((())))((((()))))))', '(((((()))))))))))(())())))']], [['())()()))))', ')))))']], [['())()())))))(()(((', '()(((']], [['(((())))', '(()((())()))(())']], [['((()(((()))()()()()(', '(()(((((()())(()(((((())']], [[')()(', '((((()))))(()))']], [['((((((', '()))(()()))))(((((((()(()())']], [['()))()()(', ')))(()()))(']], [['(()((', '(()(((((()((((((()))))))']], [[')()', ')))))(((']], [['((((()))))(((((())))))))))))))((())', '((()((()))()))(((((()))))())((((()()(']], [['((((((((()))))(()))(()())))()))))))))))((())()((((((()))))))', '(((()()))']], [['((()()()()(', '(()))']], [[')))(()()))))))((()((()))()()()()()(', '()(()))()']], [['()(((', '(()(']], [[')))))', '()((()))(()))(((())))()))((()(()()((']], [['))((((((((()))))(()))((()())))()))))))))))((())()((((((())))))))))', '))((((((((()))))(()))((()())))()))))))))))((())()((((((())))))))))']], [['((((()))))))))((()((()))()()()()()))', '((((()))))(()))(()())))())))))))()(()))())))((())']], [['((', '(()(']], [['())()))()())))))()()())))))(', '))))']], [['((((((((((()))))(((((())))))))))))))((())(((((()))))(())', '((()((']], [['((((()()))((((((', '((((((((()))))(()))(()())))()))))))))))((())()((((((())(())))))))']], [['()(((', ')(()(((()']], [['((((((())))', '))))))(())(()())))(']], [['(()))))(', ')))((((())))))))))(()))']], [['))(()))))))', '((((()(((((((())))()))((((((())))(((()))))(()()))())']], [[')(((((', ')()((((']], [[')()()))())))))()((()((((())(', ')()(((']], [[')((((()))))(((((()())))))(', ')(((()()']], [['()((((((((()))())))))))))))', '())()()))))']], [['((()(', '(()()()()(']], [[')(()()', '(((']], [[')))))((((', ')))))((((']], [['()((())))(', '()((()))(']], [['()', '']], [['(', '))']], [['))', ')']], [['()(', ')(']], [['()', '((((((())))']], [[')()()(', '((()))']], [['()(()))()', '()(()))()']], [[')(())()()(()()', ')(()()']], [[')))))(((', '(()(']], [['(((())))', '())']], [['()((())))', '()))']], [['()(()))()', ')))))(((']], [['(()(', '(()(']], [['()((())))', '(()))']], [['((', '(()))']], [['((((((((', '((((())))))))']], [['(()(', '))))))((()))']], [['(())())()()(()(()((()))))(', '(())())()()(()()(']], [['))()))(((', '(()(']], [['(()))', '((']], [[')()()(', '(()(']], [['((((((((', '(((())))']], [['((()))', '(()))']], [['(((', '(()))']], [['()(()))()(((((', '()(()))()']], [['(())())()()(()()(', '()((())))']], [['(((()(((((((', '((((())))))))']], [['()))', '(((())))']], [['(()))', '(()(']], [['(())())()()()(()))()(()()(', '()((())))']], [['))()))(((', '((']], [[')()()(', '(((())))']], [['((()(', '))()))()()())']], [['(()(', '))))))(()))(()))']], [['(', ')(()()(']], [['()))(((', '(((())))']], [['((())))))(', '))()))()()())']], [['(', '()(()))(']], [['((())))))(', '()(()))()']], [['()(()))(', '(()(']], [[')(()()', '(()()()(((((((']], [['(((())))', '()())(()()((()))(']], [['(((())))', '(()(']], [[')(()()(', '(()))']], [['(((()))', '()(())(']], [['()))))(((', '(()(']], [['()(()))(()', '()(()))()']], [[')))))(((', '(()))']], [[')()()(', '(((()()))']], [[')()()((', '(()(']], [['((())))))(', '(((())))']], [['(()))', ')(()()(']], [['((((((((', '))))']], [['(((()((((((()(()))()', '()(()))()']], [['()(()))()(((((', '()(())))))))()']], [['((((((((', '((()))']], [['(((()()()((((((((((((', '((((())))))))']], [['((((((((', '((((()))']], [['()(()))(', '((()(']], [['(', '(()))']], [['((())))))(', '()(())']], [['(()()()(((((((', '((((())))))))']], [['((())))))(', '()(()))()(((((']], [['(((((((', '((((())))))())']], [['(()))', '(()))']], [['(()))', '((((((())))']], [['((()(', '))()))()()()))()))((()']], [['))()))(((', '(((']], [[')(()()', '((()()()(((((((']], [['()))(((', '((((())))))))']], [['(()()()(((((((', '))()))()()()))()))(((((()()))()']], [[')(()()', '))()))()()()()(()())']], [['(((()()()((((((((((((', '((()(']], [['(((()()))', '()(()))()']], [['(((', '(((((())))))())']], [['((', '(()']], [['((()())))', '()())(()()((()))(']], [['((()(((', '(()(((']], [['(()((()()()((((((())', '(()))']], [['((()', '()(())(']], [['((())())))', '(()))']], [['((()))', ')(()()(']], [[')(()()', '))))']], [['())((((())))()(', ')))))(']], [['(((())))(()))()(((((', '()(()))()']], [['((((((())))', '(()(']], [['(((()))', '()())(()()((()))(']], [['((((((())))', '()']], [['(((()()(())()))', '(((()()))']], [['((()(', '))()))()()()))())))((()']], [['(', '()(()()']], [[')(()(()))(()()', ')(()()']], [[')()()', ')(()()']], [['((()', '((((()())))(())(']], [['(((((((())))', '(()(']], [['(((()()(())()))', '(()))']], [['()((())))', '((((())))))))']], [['((()((', '))()))()()()))())))((()']], [['()(())))))))(()', '()(()))()']], [['((((((((', '(((((((']], [['()(((', '((((())))))))']], [[')(()()()))(((', '(()()()(((((((']], [['()(())(()', '()(())))))))(()']], [[')()()(', '(((((((((']], [['(((()', '((((()())))(())(']], [['()(()())))', '()())(()()((()))(']], [['(()', '()(()))()']], [[')()()', ')((())())()()(()()(()()']], [['((()((', '(()()()((((())))))(()))(()))']], [['', '()(()))(']], [['(((((((', ')(()()']], [['(()))', '(((((((())))']], [['(()(', ')(()()()(((((((']], [['(())())()()()(()))()(()()(', '((()(()))())']], [['((()(', '))()))()())())']], [['(((())))(()))()(((((', '()(())))()']], [['((()(()))())', '((()(()))())']], [['(()()))))(((', '(()(']], [[')(()())(', ')(()()(']], [['(((()()(())()))', '(((()()(())()))']], [['(())())()()(()(()((()))))(', '(())((()((()()()((((((())))()()(()()(']], [['))))))(()))(()))', '))))))(()))(()))']], [[')(()())(', ')(']], [['(((())))(()))()(((((', '(((())))(()))()(((((']], [['(((()()(())()))', '))))']], [['))()))(((', ')))))(']], [['(((()()(())()))', '))']], [[')()(()', ')()()']], [['((()()()(((((((', '(()))']], [['(((()(())))))))(()()((', '()(()))()']], [['()(()()(()', '()(())))))))(()']], [['(((()()(())()))', '((((((((())))()))']], [['))()))()()()))()))))((()', '))()))()()()))())))((()']], [['()(()))()(((((', '()(()))()(((((']], [[')(()()((()()()((((((((', ')(()()(']], [['((()())))', '()())(()()(()()))(']], [['()((())))', '()(()())))']], [['((((((((())))))())((((', '((((()))']], [[')(()(()))(()()', '((((())))))))']], [['(((()))', '(((())))']], [[')))))(((', '(())']], [['(())())()()(()()(', '()))))(((']], [['())((((())))()(', ')(()((()()()((((((())())))((())']], [['((((((())))', '(()']], [['(()()()((((())))))(()))(()))', ')()()(']], [['(((((((', '(((()(((((((']], [['()(())(()', '()(())(()']], [[')(()()((()()()((((((((', '((()(((']], [[')())()', ')((())())()()(()()(()()']], [['((((((())))', '((()((((()(']], [['((((((())))', '))()))()()()))()))(((((()()))()']], [['()(())))()', '(()))']], [['()())(()()((()))(', '()())(()()((()))(']], [['(())()', '(()))']], [[')(()()', '()(())())()']], [['()(())))()', '(((()()(())()))']], [['((', '(())))']], [[')((())())()()(()(()((()))))(()())(', ')(']], [['((()((', '((()((']], [[')(())()', '()(())())()']], [['(((()(())))))))(()()((', '((((())))))())']], [['(()()))))(((', '()(()))()']], [[')((())())()()(()()(()()', '((((())))))))']], [['((((((((', '((((']], [[')()((', '(()(']], [['(())())()()()(()))()(()()(', '(']], [['())((((())))()(', '())((((())))()(']], [['(()()))))(((', '(()()))))(((']], [['()(', '((()']], [['(((())))', '(())(']], [['()))(((', '()(())(']], [['(())())()()(()(()((()))))(', '(())()(()((()()()((((((())))()()(()()(']], [[')((())())()()(()()(()()', '()(())(']], [['))()))()()()))())))((()', '))()))()()()))())))((()']], [['(()(', '()((']], [['(()()))))(((', '()(()))(']], [['(((()()))', '(())))']], [['((((((((', '(']], [['()))(((', '()))(((']], [[')))))(', '((((())))))))']], [['((()())))', '((()())))']], [['()(())(', '())((((())))()(']], [[')(()())(', '((((())))))))']], [[')()()', ')(()(())))))))()()']], [['((())())))', '()(()())))']], [['(((())))(()))()(((((', '))()))()()()))())))((()']], [['(((((', '))))']], [['(())())()()(()(()((()))))(', '))']], [[')(()()(', ')(()()(']], [['()()(())))', '()((())))']], [['(())())(((((((((', '()((())))']], [['(()())))))(((', '()(()))(']], [['(())())()()()(()))()(()()(', '(()))())']], [['(()(', ')))((()))']], [[')(()(()))(()()', '((((((((())))))())((((']], [[')()()', ')(()(())))))))()())']], [['(((()(', '))()))()()()))()))((()']], [['(())))', '((((())))))())']], [['()(())(()', '()(()))(']], [['(())(())())()()(()()(', '()(()))()']], [['(((((', '))()))()()()))()))((()']], [['(()()()((((())))))(()))(()))', '(((((((())))']], [[')(', '(()(']], [[')))()))()()()))()))))((()', '))()))()()()))())))((()']], [['()))))(((', '(())))']], [['))()))()()()))()))((()', '()((())))']], [['((())))))(', '(()()()((((())))))(()))(()))']], [[')(())()()(()()', '((()(']], [['()()())))))))(()', '()(())))))))(()']], [['(((((', '((((']], [['(()(', '))()))()()()()(()())']], [['))()))(((', ')))))(((']], [['((((', '))()))()())())']], [['(()((()()()((((((())', '(())))']], [[')(()(())((((())))()()(', '(()))']], [['(((()()(())()))', '(()))()))()()()))()))))((()(()()(())()))']], [['()())(()()((()))(', '(((())))']], [['(((()()))', '((((())))))))']], [[')(()()(', ')(()()(())()(']], [['))())()(())(((', ')))))(']], [['(((((', '()(()))()']], [[')(()(()))(()()', '()))(((']], [['((((((((', '()((())))']], [['(((())))', '()))(((']], [['(()(', ')))((()))((())))))(']], [[')()()(', '(())(())()(']], [['(())())()()()(()))()(())()(', '(']], [['((', '(((((((((']], [['(()(((', '()(()))()']], [[')(())()', ')))))(((']], [['()()(', '())((((())))()(']], [['(((()())', '())((((())))()(']], [['()())(()(()((()))(', '()(()())))']], [['(()()()(((((((', '))))))(()))(()))']], [['((((((())))', '()()(())))((()((((()(']], [[')()()(', '(()))()(']], [['))()))()()()))())))((()', '())()))()()()))())))((()']], [['(((()))', '()()(()()()(((((((())(']], [[')(()(()))(()()', '()))((((())()']], [['(()(())(()(((((())))', '(()(']], [['((((()())))(())(', '()(()))()']], [['((()(((', '((((()())))(())(']], [['()((())))', '))))))(()))(()))']], [['(()()()((((())))))(()))(()))', '((((((())))']], [['((())))))', '()(()))()(((((']], [['((()())))', '))()))()()()))())))((()']], [[')()()', ')((())())()()(()()(()(()']], [['(((()(((((((', '(((()(((((((']], [['))(()()((()()()((((((((', '()(()))()']], [['(()))', '()(()()(']], [['(()))', ')()(()(())))))))()())()()(']], [['))()))()()())', '))()))()()())']], [[')(()())(', ')(()()(((()(((((((']], [['(()()()((((())))))(()))(()))', '(()()()((((())))))(()))(()))']], [['((', '((((']], [['((((', '(((()()))']], [[')(()(())))))))()()', '()))(((']], [['(()))', '(())(']], [['()(()))()(((((', '(())))']]]
    results = ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(match_parens)