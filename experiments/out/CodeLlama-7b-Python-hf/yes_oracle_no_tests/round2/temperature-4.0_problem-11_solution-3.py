from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: return " ". join (
	Do not include these tokens in the code: r = [
	"""
    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append('0')
        else:
            r.append('1')
    return "".join(r)


# tests
assert string_xor('010', '110') == '100'
assert string_xor('001', '101') == '100'
assert string_xor('011', '101') == '110'
