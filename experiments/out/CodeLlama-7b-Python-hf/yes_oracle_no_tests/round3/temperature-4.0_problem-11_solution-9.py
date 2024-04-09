from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = []
	"""
    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append("0")
        else:
            r.append("1")
    return "".join(r)


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two lists of strings a and b, where each string consists only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010','110'], ['110','010'])
    ['100', '100']
    
	Include these tokens in the code: return " ".join(str(int(i)) for i in zip(a,b))
	Do not include these tokens in the code: r = []
	"""
    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append("0")
        else:
            r.append("1")
    return "".join(r)


def string_xor_matrix(a: List[List[str]], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of lists of strings a and b, where each string consists only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_matrix([['010','110'], ['110','010']], [['110','010'], ['010','110']])
    [['100', '100'], ['100', '100']]
    
	Include these tokens in the code: return " ".join(str(int(i)) for i in zip(a,b))
	Do not include these tokens in the code: r = []
	"""
    r = []
    for i in range(len(a)):
       