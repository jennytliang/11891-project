from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [
	Do not include these tokens in the code: _
	"""

    return "".join(str(int(x) ^ int(y))
                   for x, y in zip(a, b))


def string_xor_(a: str, b: str) -> str:
    return "".join(str(int(bool(int(x) ^ int(y))))
                   for x, y in zip(a, b))


def bitwise_xor(a: int, b: int) -> int:
    """
    Input are two numbers a and b where only digits 1 and 0 are used, and every digit
    has one and only one leading 1.

    Perform bitwise XOR on these inputs and return result as an integer.
    >>> bitwise_xor(42, 83)
    131

    Include these tokens in the code: _________________________________
    """

    assert 0 <= a < 1_000_000_000
    assert 0 <= b < 1_000_000_000
    return sum(x ^ y for x, y in zip(bin(a)[2:], bin(b)[2:]))


if __name__ == "__main__":
    import doctest

    # 1: Test the cases
    doctest.testmod()
    
    # 2: Input/Output
    S = input()
    T = input()
    print(string_xor(S, T))
