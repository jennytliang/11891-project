from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    res = [numbers[0]]
    max_so_far = numbers[0]
    for i in range(1, len(numbers)):
        max_so_far = max(max_so_far, numbers[i])
        res.append(max_so_far)
    return res


def solution(numbers: List[int]) -> Tuple[int, int]:
    rolling_max_numbers = rolling_max(numbers)
    min_cost = min(rolling_max_numbers)
    return min_cost, numbers.index(min_cost)

