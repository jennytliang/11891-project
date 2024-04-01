from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers_set = set()
    result_list = list()
    for item in numbers:
        if item in numbers_set:
            continue
        numbers_set.add(item)
        result_list.append(item)
    return result_list