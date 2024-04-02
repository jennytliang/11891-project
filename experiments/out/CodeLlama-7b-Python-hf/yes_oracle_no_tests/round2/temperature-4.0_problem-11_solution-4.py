from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    r = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            r += "0"
        else:
            r += "1"
    return r


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists a and b consisting of strings.
    Perform binary XOR on these inputs and return result also as a list.
    >>> string_xor_list(['010', '101'], ['110', '010'])
    ['100', '110']
    """
    result = []
    for i in range(len(a)):
        result.append(string_xor(a[i], b[i]))
    return result
