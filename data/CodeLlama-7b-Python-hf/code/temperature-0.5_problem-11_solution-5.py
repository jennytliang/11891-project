from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    return "".join(str(int(a_i) ^ int(b_i)) for a_i, b_i in zip(a, b))


def string_xor_all(strings: List[str]) -> str:
    """ Input is a list of strings consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_all(['010', '110'])
    '100'
    """
    if len(strings) == 1:
        return strings[0]
    return string_xor(strings[0], string_xor_all(strings[1:]))
