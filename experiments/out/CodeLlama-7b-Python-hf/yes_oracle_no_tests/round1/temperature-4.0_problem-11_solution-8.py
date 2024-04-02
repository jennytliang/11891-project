from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    
	Include these tokens in the code: " ". join ( str
	"""

    r = []
    for i in range(len(a)):
        if a[i] == b[i]:
            r.append(str(0))
        else:
            r.append(str(1))
    return " ".join(r)


def string_xor_all(strings: List[str]) -> str:
    """ Input is a list of strings. Perform binary XOR on all pairs of strings 
    and return result also as a string.
    >>> string_xor_all(['010', '110'])
    '100'
    
	Include these tokens in the code: " ". join ( str
	"""

    if len(strings) == 0:
        return ""
    elif len(strings) == 1:
        return strings[0]
    else:
        return string_xor(strings[0], strings[1]) + " " + string_xor_all(strings[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
