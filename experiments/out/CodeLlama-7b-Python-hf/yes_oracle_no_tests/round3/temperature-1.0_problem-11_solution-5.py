from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: [ i ])
	Do not include these tokens in the code: _ bit )
	"""



    return "".join(st[0] for st in zip(a,b) if st[0] == st[1])