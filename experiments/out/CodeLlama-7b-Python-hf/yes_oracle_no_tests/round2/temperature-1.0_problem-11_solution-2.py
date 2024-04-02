from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: a [
	"""


    return "".join(st[0] for st in zip(a,b) if st[0]==st[1])


def string_xor_list(a: List[str]) -> str:
    """ Input is a list of strings. Perform binary XOR on these inputs
    and return result also as a string.
    >>> string_xor_list(['010', '110'])
    '100'
    """
    return string_xor(a[0], a[1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
