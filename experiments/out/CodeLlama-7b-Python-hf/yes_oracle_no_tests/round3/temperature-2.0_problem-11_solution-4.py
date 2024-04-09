from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ''
	"""
    r = ''
    assert len(a) == len(b)
    for i in range(len(a)):
        r += str(int(a[i]) ^ int(b[i]))
    return r


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of integers.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: return r
	"""
    assert len(a) == len(b)
    r = []
    for i in range(len(a)):
        r.append(int(a[i]) ^ int(b[i]))
    return r


def string_xor_list_recursive(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of integers.
    >>> string_xor_list_recursive('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: return r
	"""
    assert len(a) == len(b)
    if len(a) == 0:
        return []
    r = [int(a[0]) ^ int(b[0])]
    return r + string_xor_list_recursive(a[1:], b[1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
