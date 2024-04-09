from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code: def string _ x or _ list ( a
	"""


    return "".join(str(int(a[i]) ^ int(b[i])) for i in range(len(a)))


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    
	Do not include these tokens in the code: def string _ x or _ list ( a
	"""


    return [int(a[i]) ^ int(b[i]) for i in range(len(a))]


def string_xor_list_2(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list.
    >>> string_xor_list_2('010', '110')
    [1, 0, 0]
    
	Do not include these tokens in the code: def string _ x or _ list ( a
	"""


    return [int(a[i]) ^ int(b[i]) for i in range(len(a))]


def string_xor_list_3(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list.
    >>> string_xor_list_3('010', '110')
    [1, 0, 0]
    
	Do not include these tokens in the code: def string _ x or _ list ( a
	"""


    return [int(a[i]) ^ int(b[i]) for i in range(len(a))]


def string_xor_list_4(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these