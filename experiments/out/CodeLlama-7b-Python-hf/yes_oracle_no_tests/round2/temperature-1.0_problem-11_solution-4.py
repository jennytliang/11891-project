from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: a [ i ])
	Do not include these tokens in the code: x )
	"""


    return "".join(st for st in "{:b}".format(int(a,2)^int(b,2))[:1:-1])

if __name__ =='__main__':
    import doctest
    doctest.testmod()