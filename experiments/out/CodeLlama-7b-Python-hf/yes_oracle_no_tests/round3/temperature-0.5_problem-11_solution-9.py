from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""



    return "".join(st[0] if st[0] == st[1] else "1" for st in zip(a, b))


def string_xor_list(a: List[str], b: List[str]) -> List[str]:
    """ Inputs are two lists a and b of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a list of strings.
    >>> string_xor_list(['010', '110'], ['110', '110'])
    ['100', '000']
	"""
    return [string_xor(a[i], b[i]) for i in range(len(a))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
