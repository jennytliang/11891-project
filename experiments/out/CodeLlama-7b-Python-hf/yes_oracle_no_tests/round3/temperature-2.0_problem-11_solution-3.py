from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: ".
	"""

    ret_str = ""

    for i in range(len(a)):
        if a[i] == b[i]:
            ret_str += "0"
        else:
            ret_str += "1"

    return ret_str


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two list of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '001'], ['110', '101'])
    ['100', '100']
    
	Include these tokens in the code: ".
	"""

    ret_list = []

    for i in range(len(a)):
        ret_list.append(string_xor(a[i], b[i]))

    return ret_list
