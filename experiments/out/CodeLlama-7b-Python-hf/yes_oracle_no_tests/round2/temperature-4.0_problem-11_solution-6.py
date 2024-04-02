from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    return " ".join(str(int(a, 2) ^ int(b, 2)))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input are two list of strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '010'], ['110', '001'])
    ['100', '011']
    
	Include these tokens in the code: return " ". join ( str ( int ( a
	Do not include these tokens in the code: r = ""
	"""
    return [" ".join(str(int(a[i], 2) ^ int(b[i], 2))) for i in range(len(a))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
