from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list(['010', '110'], ['110', '010'])
    ['100', '000']
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    return ["".join(str(int(a[i][j]) ^ int(b[i][j])) for j in range(len(a[i]))) for i in range(len(a))]


def string_xor_list_2d(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of lists of strings.
    >>> string_xor_list_2d([['010', '110'], ['110', '010']], [['110', '010'], ['010', '110']])
    [['100', '000'], ['000', '100']]
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    return [["".join(str(int(a[i][j]) ^ int(b[i][j])) for j in range(len(a[i]))) for i in range(len(a))] for j in range(len(a))]


if __name__ == "__main__":
    import do