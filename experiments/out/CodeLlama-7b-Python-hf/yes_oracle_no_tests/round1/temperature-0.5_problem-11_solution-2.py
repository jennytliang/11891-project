from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code:  return " ". join ( str ( int (
	"""

    return "".join([f"{int(a[i]) ^ int(b[i]):b}" for i in range(len(a))])


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Input is two lists of strings a and b that consist only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['101', '011'])
    ['111', '100']
    """
    return ["".join([f"{int(a[i][j]) ^ int(b[i][j]):b}" for j in range(len(a[i]))]) for i in range(len(a))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
