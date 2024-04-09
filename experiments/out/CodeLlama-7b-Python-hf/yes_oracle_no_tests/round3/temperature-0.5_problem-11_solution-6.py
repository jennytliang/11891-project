from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code: def string _ x or _ list ( a
	"""



    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_list(a: str, b: List[str]) -> List[str]:
    """ Input is a string a and a list of strings b.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list('010', ['110', '100', '101'])
    ['100', '010', '011']
    
	Do not include these tokens in the code: def string _ x or _ list ( a
	"""



    return ["".join(str(int(a[i]) ^ int(b[j][i])) for i in range(len(a))) for j in range(len(b))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
