from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: result = ''
	"""
    return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of integers.
    >>> string_xor_list('010', '110')
    [1, 0, 0]
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: result = ''
	"""
    return [int(a[i]) ^ int(b[i]) for i in range(len(a))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
