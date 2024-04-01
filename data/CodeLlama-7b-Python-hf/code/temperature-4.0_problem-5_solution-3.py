from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    new_list = [delim if index != 0 else number if index + 1 < len(numbers) is None else number else delim if index + i <= len(numbers) else delim*i for i, number in enumerate(numbers)]
    return 0 