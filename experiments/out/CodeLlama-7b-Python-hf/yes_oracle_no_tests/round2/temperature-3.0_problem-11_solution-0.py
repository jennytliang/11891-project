from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code: def string _ x or _ 2 ( a
	"""

    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_list(a: str, b: List[str]) -> List[str]:
    """ Input is a string a and a list of strings b.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list('010', ['001', '101', '111'])
    ['011', '010', '010']
    
	Do not include these tokens in the code: def string _ x or _ 2 ( a
	"""

    return [a] + [string_xor(a, b) for b in b]


def string_xor_all(a: str, b: List[str]) -> str:
    """ Input is a string a and a list of strings b.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_all('010', ['001', '101', '111'])
    '010'
    
	Do not include these tokens in the code: def string _ x or _ 2 ( a
	"""

    return a


def string_xor_all_list(a: str, b: List[str]) -> List[str]:
    """ Input is a string a and a list of strings b.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_all_list('010', ['001', '101', '111'])
    ['011', '010', '010']
    
	Do not include these tokens in the code: def string _ x or _ 2 ( a
	"""

    return [a] + [string_xor(a, b) for b in b]


def string_xor_all_list_2(a: str, b: List[str]) -> List[str]:
    """ Input is a string a and a list of strings b.
    Perform binary XOR on these inputs and return result also as