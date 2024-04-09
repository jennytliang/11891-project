from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: ret = ''
	"""
    ret = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            ret += '1'
        else:
            ret += '0'
    return ret


def string_xor_list(a: List[str]) -> str:
    """ Input is a list of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_list(['010', '110'])
    '100'
    """
    ret = ''
    for i in range(len(a[0])):
        count = 0
        for j in range(len(a)):
            if a[j][i] == '1':
                count += 1
            else:
                count -= 1
        if count == 0:
            ret += '0'
        else:
            ret += '1'
    return ret


def string_xor_list_2(a: List[str]) -> str:
    """ Input is a list of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_list_2(['010', '110'])
    '100'
    """
    return ''.join(['1' if a.count('1') % 2 == 1 else '0' for a in zip(*a)])


def string_xor_list_3(a: List[str]) -> str:
    """ Input is a list of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_list_3(['010', '110'])
    '100'
    """
    return ''.join(['1' if a.count('1') % 2 == 1 else '0' for a in zip(*a)])


def string_xor_list_4(a: List[str]) -> str: