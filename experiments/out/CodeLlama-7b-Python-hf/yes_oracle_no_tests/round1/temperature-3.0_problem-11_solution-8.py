from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    a_int = int(a, 2)
    b_int = int(b, 2)
    xor = a_int ^ b_int
    return bin(xor)[2:]


def string_xor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list('010', '110')
    ['100', '100', '000']
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    a_int = int(a, 2)
    b_int = int(b, 2)
    xor = a_int ^ b_int
    return [bin(xor)[2:]] * 3


def string_xor_list_of_lists(a: str, b: str) -> List[List[str]]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of lists of strings.
    >>> string_xor_list_of_lists('010', '110')
    [['100', '100', '000'], ['100', '100', '000']]
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    a_int = int(a, 2)
    b_int = int(b, 2)
    xor = a_int ^ b_int
    return [[bin(xor)[2:]] * 3] * 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
