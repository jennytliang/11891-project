from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    if numbers is None or isinstance(numbers, str) or not isinstance(numbers, List):
        raise TypeError('Input should be a list only')
    else:
        for element in numbers:
            if not isinstance(element, int) or (element % 1):
                raise TypeError('Element should be of type integer')

    interspersed_list: List[(int)] = []
    for num in range(len(numbers)):
        if num == len(numbers) - 1:
            interspersed_list.append(numbers[num])
        else:
            interspersed_list.append(numbers[num])
            interspersed_list.append(delimeter)
    return interspersedList