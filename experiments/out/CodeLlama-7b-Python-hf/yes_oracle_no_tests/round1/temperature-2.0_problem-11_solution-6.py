from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            r += "0"
        else:
            r += "1"
    return r


def string_xor_all(a: str, b: str, c: str) -> str:
    """ Input are three strings a, b, and c consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_all('010', '110', '101')
    '001'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = ""
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            r += "0"
        elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
            r += "1"
        else:
            r += "0"
    return r


def string_xor_all_list(a: str, b: str, c: str) -> List[str]:
    """ Input are three strings a, b, and c consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_all_list('010', '110', '101')
    ['001', '100', '011']
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""
    r = []
    for i in range(len(a)):
        if a[i] == b[i] == c[i]:
            r.append('0')
        elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
            r.append('1')
        else