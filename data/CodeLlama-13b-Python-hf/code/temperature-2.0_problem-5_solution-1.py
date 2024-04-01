from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    numbers.insert(0, 0)
    numbers.append(0)
    output = []
    for i in range(len(numbers) - 1):
        if i % 2 == 0:
            output.append(numbers[i])
        else:
            output.append(delimeter)
            output.append(numbers[i])
    return output[:-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
