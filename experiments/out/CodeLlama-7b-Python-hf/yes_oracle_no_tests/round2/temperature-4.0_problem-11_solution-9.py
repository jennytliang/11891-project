from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append('0')
        else:
            r.append('1')
    return ''.join(r)


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '111'], ['110', '001'])
    ['100', '111']
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    if len(a) != len(b):
        raise ValueError("a and b must be of equal length")
    for i in range(len(a)):
        r.append(string_xor(a[i], b[i]))
    return r


def string_xor_list_of_lists(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of lists of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_list_of_lists([['010', '111'], ['110', '001']], [['110', '001'], ['010', '111']])
    [['100', '111'], ['100', '001']]
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = [] for
	"""
    r = []
    if len(a) != len(b):
        raise ValueError("a and b must be of equal length")
