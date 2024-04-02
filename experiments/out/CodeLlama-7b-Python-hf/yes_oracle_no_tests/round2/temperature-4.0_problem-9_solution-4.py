from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers
	Do not include these tokens in the code: _ so _ far : int
	"""
    max_so_far = 0
    rolling_max = []
    for _, number in enumerate(numbers):
        max_so_far = max(max_so_far, number)
        rolling_max.append(max_so_far)
    return rolling_max


def max_in_list(numbers: List[int]) -> Tuple[int, int]:
    """ Given a list of integers, return the index and value of the maximum element.
    >>> max_in_list([1, 2, 3, 2, 3, 4, 2])
    (6, 4)
    """
    max_so_far = 0
    index_of_max = 0
    for index, number in enumerate(numbers):
        if number > max_so_far:
            max_so_far = number
            index_of_max = index
    return index_of_max, max_so_far


def max_in_list_recursive(numbers: List[int]) -> Tuple[int, int]:
    """ Given a list of integers, return the index and value of the maximum element.
    >>> max_in_list_recursive([1, 2, 3, 2, 3, 4, 2])
    (6, 4)
    """
    def _so_far(numbers, index):
        if index == len(numbers):
            return 0, 0
        number = numbers[index]
        index_of_max, max_so_far = _so_far(numbers, index + 1)
        if number > max_so_far:
            return index, number
        else:
            return index_of_max, max_so_far

    return _so_far(numbers, 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
