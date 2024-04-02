from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    # xor_str = ''
    # for i in range(len(a)):
    #     if a[i] == b[i]:
    #         xor_str += '0'
    #     else:
    #         xor_str += '1'
    # return xor_str
    return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def string_xor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    xor_list = []
    for i in range(len(a)):
        if a[i] == b[i]:
            xor_list.append('0')
        else:
            xor_list.append('1')
    return xor_list


def string_xor_list_comprehension(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these tokens in the code: x or _ list = []
	"""
    return [str(int(a[i]) ^ int(b[i])) for i in range(len(a))]


def string_xor_list_map(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    
	Include these tokens in the code: return " ". join ( str ( int
	Do not include these