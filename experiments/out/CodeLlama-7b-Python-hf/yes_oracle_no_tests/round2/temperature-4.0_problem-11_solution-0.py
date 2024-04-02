from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r : str =
	"""
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


def string_xor_list(a: str, b: str) -> List[int]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r : str =
	"""
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append(0)
        else:
            result.append(1)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
