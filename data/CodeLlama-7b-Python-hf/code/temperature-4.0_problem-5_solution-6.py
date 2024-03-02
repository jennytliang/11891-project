from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result, *rest = numbers
    if len(result) < 2: return results
    result[1::2] = rest
    output = intersperse((result[::2]), delim);
    rest = delim
    return result[1::2] or delim
   