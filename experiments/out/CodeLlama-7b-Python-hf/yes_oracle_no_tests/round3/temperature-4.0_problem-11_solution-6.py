from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: ".
	Do not include these tokens in the code: join ( str ( int ( a ,
	"""

    ret = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ret += "0"
        else:
            ret += "1"
    return ret


def string_xor_list(a: str, b: str) -> List[str]:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor_list('010', '110')
    ['100']
    """
    ret_list = []
    ret = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ret += "0"
        else:
            ret += "1"
    ret_list.append(ret)
    return ret_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
