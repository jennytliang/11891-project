from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: )):
	Do not include these tokens in the code: ) - 1 ):
	"""

    res = []
    for i in range(len(nu) - 1):
        res.extend([nu[i], delimeter])
    res.append(nu[-1])
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
