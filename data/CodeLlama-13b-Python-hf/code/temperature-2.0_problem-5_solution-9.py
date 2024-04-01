from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers.insert(0, delimeter)
    numbers.insert(0, delimeter)

    for i in range(3, len(numbers), 2):
        numbers.insert(i, delimeter)

    return numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
