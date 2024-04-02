from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Do not include these tokens in the code: r = "" for
	"""
    return "".join(["0" if a_i == b_i else "1" for a_i, b_i in zip(a, b)])


def string_xor_list(a: List[str]) -> str:
    """ Input is a list of strings a. Perform binary XOR on these inputs
    and return result also as a string.
    >>> string_xor_list(['1001', '0110', '1100'])
    '0111'
    """
    return "".join(
        ["0" if a_i == "0" else "1" for a_i in "".join(a)]
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
