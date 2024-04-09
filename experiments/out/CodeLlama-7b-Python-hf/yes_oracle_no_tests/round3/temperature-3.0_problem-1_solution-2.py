from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    
	Include these tokens in the code: c nt , group , results
	Do not include these tokens in the code: n t
	"""

    results = []
    group = ''

    c = 0
    n = 0

    for char in paren_string:
        if char == '(':
            c += 1
        elif char == ')':
            c -= 1
            n += 1
        if c == 0 and n == 1:
            results.append(group)
            group = ''
            n = 0
        group += char

    return results


def main():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups('()((())((())))') == ['()', '()()()', '(())', '(()())']
    assert separate_paren_groups('()((())((())))(())') == ['()', '()()()', '(())', '(()())', '()']
    assert separate_paren_groups('(((())())())') == ['(()())', '()']
    assert separate_paren_groups('(())((())((())))(())') == ['()', '()()()', '(())', '(()())', '()']
    assert separate_paren_groups('((((()))))') == ['(()())']
    assert separate_paren_groups('(((((((((()))))(((((()))))))))))') == ['(((((((((()))))(((((()))))))))))']
    assert separate_paren_groups('(((((((((()))))(((((()))))))))))()') == ['(((((((((()))))(((((()))))))))))', '()']
    assert separate_paren_groups('(((((((((()))))(((((()))))))))))(((((((((()))))(((((()))))))))))') == [
        '(((((((((()))))(((((()))))))))))', '(((((((((()))))(((((()))))))))))']
    assert separate_paren_groups('(((((((((()))))(((((()))))))))))(((((((((()))))(((((()))))))))))()') == [
        '(((((((((()))))((