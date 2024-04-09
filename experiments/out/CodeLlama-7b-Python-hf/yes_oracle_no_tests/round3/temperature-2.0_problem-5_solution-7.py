from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    
	Include these tokens in the code: numbers )):
	Do not include these tokens in the code: nu ) - 1 ):
	"""


    res = []
    for i in rang(len(numbers)):
        if i == 0:
            res.append(numbers[i])
        else:
            res += [numbers[i], delimeter]
    return res


def run_tests():
    """
    >>> all([intersperse([], 4) == [],
    ...      intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]])
    True
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
