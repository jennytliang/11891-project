from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    
	Include these tokens in the code:   def count _ depth ( s
	Do not include these tokens in the code: # TODO : implement your solution here
	"""

    def count_depth(s: str, depth: int = 0) -> int:
        """
        The function counts the depth of each substring in the input string.
        """
        if s == '':
            return depth
        if s[0] == '(':
            return count_depth(s[1:], depth + 1)
        else:
            return count_depth(s[1:], depth - 1)

    return [count_depth(s) for s in paren_string.split()]


if __name__ == "__main__":
    print(parse_nested_parens('(()()) ((())) () ((())()())'))




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
    inputs = [['(()()) ((())) () ((())()())'], ['() (()) ((())) (((())))'], ['(()(())((())))'], [''], ['((()))'], ['(())(()())'], ['(())(()(()))((()()))'], ['(()()(((())))(()(())))()'], ['()((()))'], ['(())'], ['()()()'], ['()(())'], ['(((())(()(()))((()()))))(()(()))((()()))'], ['(()()(()(())((()()(((())))(()(())))())(((()))))(()(())))()'], ['((()(())(()(()))((()()))))'], ['(()()(((())))(()(())(((())(()(()))((()()))))(()(()))((()()))))()'], ['((()()(((())))(()(())))())((()()))'], ['(()()(((())((()()(((())))(()(())))())(((()))))(()(()))))()'], ['()(()()(((())))(()(())(((())(()(()))((()()))))(()(()))((()()))))()((()))'], ['((()(())((()(()))((()())))))'], ['((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))'], ['((((((())(())))())((()()()(()(((()(()))))))))()(((())(()(()))((()()()))()))((()))()(()))()'], ['()()()()()()'], ['((((((()))(()()((()))))(()))))'], ['(((())))'], ['((()())()())'], ['()()()()()'], ['((((())()))()(()))(())'], ['((())()()()((((())(())))))'], ['(((((((()()()((()))(())()((()))((()())(())))))))()())()())'], ['((((())())))(())(())'], ['()(((())))'], ['(((((((())))))))'], ['(((((()(((()))))(()))()()())(())))()(())(())'], ['((())())()()'], ['((())()()((((())(())))))'], ['(()(())()())'], ['((((())(())))()()())((()))(())'], ['((()))()()()'], ['((((())())))(())'], ['(((((((((((((((())))))))))))))))'], ['((((((((((((())()()()))()))))(()))(())))))'], ['(((((((())((((())(())))))))())))()'], ['((((())((())))()(())))'], ['((((((((((()))))))((()))()))))'], ['(()(())())'], ['()'], ['((((((((((())))))))((()))((((((((())((((())(())))(((()()((())((()))(()((((()))()())))))())((((())))((()((((((())))))))))())))))()((((())))))))))))'], ['((((((((()(()))))))(((()))()))))'], ['((((((((((((((()))))))((()))()))))))))'], ['((((((((((((((()))))))((()))())((((((((()(()))))))(((()))())))))))))))'], ['((((())())(((((((())((((())(()))))(((()()((())((()))(()((((()))()())))))())((((())))((()((((((())))))))))())))))()((((()))))))))(())(())'], ['((((())((()))())(())))'], ['((())()())'], ['()()()()()((((((((((()))))))((()))()))))()'], ['((((((((((())))))((()))))(()))))'], ['((((((((((())))))))((()))((((((((())((((())(())))(((()()((())((()))(()((((()))()())))))())((((()))))((()(((((((())))))))))())))))()((((())))))))))))'], ['((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()((((()))))))))))((((((()()()((()))(())()(((((())))))))))))'], ['(((((()()()((()))(())()((()))())))))(()((((((((((()))))))((())))))))'], ['((((((()))(()()((())))))))'], ['(((((((()))))(()))))'], ['()()()()'], ['(((((()()()((()))(())()((()))((()())((((((()))(()()((()))))(()))))(())))))))'], ['((((((()))(()()((())(((((()()()((()))(())()((()))((()())(())))))))))))))'], ['(((())((((((()(()))))))((((((((((((()))))))((())(()))())))((()))))))((()))))'], ['((((((((()(())))()))(((())))()))))'], ['((((((((((()))))))((()))())))((())()()))'], ['(((((((())((((())(())))(((()()((())((()))(()(((((()))()())))))))((((())))((()((((((())))))))))())))))())((((()))))))'], ['(((((((((())((((())(())))(((()()((())((()))(()((((()))()())))))())((((())))((()((((((())))))))))())))))()((((()))))))((((())())))(())(())((((((((()))))))((())))())))((())()()))']]
    results = [[2, 3, 1, 3], [1, 2, 3, 4], [4], [], [3], [2], [3], [5], [3], [2], [1], [2], [5], [8], [5], [7], [6], [9], [7], [6], [11], [10], [1], [8], [4], [3], [1], [5], [6], [10], [5], [4], [8], [9], [3], [6], [3], [5], [3], [5], [16], [13], [11], [6], [11], [3], [1], [22], [10], [15], [17], [19], [6], [3], [11], [11], [22], [12], [12], [8], [8], [1], [14], [14], [16], [10], [11], [18], [20]]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(parse_nested_parens)