from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: str
	Do not include these tokens in the code: st [ 0 ] for st in zip
	"""



    return "".join(str(int(i) ^ int(j)) for i, j in zip(a, b))



def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of integers.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: str, list, zip
	Do not include these tokens in the code: st [ 0 ] for st in zip
	"""



    return [int(i) ^ int(j) for i, j in zip(a, b)]



def string_xor_all(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_all('010', '110')
    '100'
    
	Include these tokens in the code: str, zip
	Do not include these tokens in the code: st [ 0 ] for st in zip
	"""



    return "".join(str(int(i) ^ int(j)) for i, j in zip(a, b))



def string_xor_all_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of integers.
    >>> string_xor_all_list('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: str, list, zip
	Do not include these tokens in the code: st [ 0 ] for st in zip
	"""



    return [int(i) ^ int(j) for i,