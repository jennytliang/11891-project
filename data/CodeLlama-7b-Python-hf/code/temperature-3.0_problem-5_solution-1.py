from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    return [n for pair in zip(numbers[::2], numbers[1::2]) for n in pair + (delimeter,)][:-1]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
