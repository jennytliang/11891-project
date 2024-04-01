from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of ints.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return [int(a_i) ^ int(b_i) for a_i, b_i in zip(a, b)]


def string_xor_list_no_zip(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of ints.
    >>> string_xor_list_no_zip('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return [int(a_i) ^ int(b_i) for a_i, b_i in zip(a, b)]


def string_xor_split(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of ints.
    >>> string_xor_split('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return [int(a_i) ^ int(b_i) for a_i, b_i in zip(a.split(), b