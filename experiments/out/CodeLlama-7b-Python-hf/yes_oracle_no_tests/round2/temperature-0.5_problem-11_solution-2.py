from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: ( str (
	Do not include these tokens in the code: ([ f " {
	"""


    return "".join(map(lambda x: str(int(x[0]) ^ int(x[1])), zip(a, b)))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists a and b containing only strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['111', '010'])
    ['101', '100']
    
	Include these tokens in the code: ( List [ str (
	Do not include these tokens in the code: ([ f " {
	"""


    return list(map(string_xor, a, b))


def string_xor_list_list(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists a and b containing only lists of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_list_list([['010', '110'], ['111', '010']], [['111', '010'], ['010', '110']])
    [['101', '100'], ['101', '100']]
    
	Include these tokens in the code: ( List [ List [ str (
	Do not include these tokens in the code: ([ f " {
	"""


    return [list(map(string_xor, x, y)) for x, y in zip(a, b)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
