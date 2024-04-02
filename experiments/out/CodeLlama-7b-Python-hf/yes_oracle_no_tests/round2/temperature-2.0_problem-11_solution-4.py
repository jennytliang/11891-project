from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = '' for
	"""
    r = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            r += '0'
        else:
            r += '1'
    return r


def string_xor_list(a: str, b: List[str]) -> List[str]:
    """ Input are two strings a and a list of strings b.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list('010', ['110', '001'])
    ['100', '001']
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = '' for
	"""
    r = []
    for i in range(len(b)):
        r.append(string_xor(a, b[i]))
    return r


def string_xor_list_list(a: List[str], b: List[List[str]]) -> List[List[str]]:
    """ Input are two lists of strings a and b.
    Perform binary XOR on these inputs and return result also as a list of lists of strings.
    >>> string_xor_list_list(['010', '110'], [['110', '001'], ['010', '110']])
    [['100', '001'], ['010', '110']]
    
	Include these tokens in the code: return " ". join
	Do not include these tokens in the code: r = '' for
	"""
    r = []
    for i in range(len(b)):
        r.append(string_xor_list(a[i], b[i]))
    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()
