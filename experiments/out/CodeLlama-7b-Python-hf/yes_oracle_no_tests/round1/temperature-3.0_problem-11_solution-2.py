from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    return ' '.join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list.
    >>> string_xor_list(['010', '110'], ['100', '010'])
    ['110', '100']
    
	Include these tokens in the code: return " ". join ( str
	Do not include these tokens in the code: x or _ list = []
	"""
    return [' '.join([str(int(a[i][j]) ^ int(b[i][j])) for j in range(len(a[i]))]) for i in range(len(a))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
