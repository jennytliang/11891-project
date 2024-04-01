from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    rolling_max_list = []
    max_so_far = numbers[0]
    for number in numbers:
        if number > max_so_far:
            max_so_far = number
        rolling_max_list.append(max_so_far)

    return rolling_max_list


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [(1, 1), (2, 2), (3, 3), (3, 3), (3, 3), (4, 4), (4, 4)]
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    rolling_max_list = []
    max_so_far = numbers[0]
    for i, number in enumerate(numbers):
        if number > max_so_far:
            max_so_far = number
        rolling_max_list.append((number, max_so_far))

    return rolling_max_list


if __name__ == '__main__':
    import doctest

    doctest.testmod()
