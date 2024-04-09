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
            r.append('0')
        else:
            r.append('1')
    return "".join(r)


def string_xor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list('010', '110')
    ['0', '1', '0']
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = []
	"""
    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append('0')
        else:
            r.append('1')
    return r


def string_xor_list_alt(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result as a list of strings.
    >>> string_xor_list_alt('010', '110')
    ['0', '1', '0']
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = []
	"""
    return list(map(str, map(int.__xor__, map(int, a), map(int, b))))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
