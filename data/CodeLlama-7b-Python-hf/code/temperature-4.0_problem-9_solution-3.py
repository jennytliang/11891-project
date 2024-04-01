from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    size = len(numbers)
    result = [None] * size
    result[0] = max([numbers[0]] + [numbers[1]])
    for i, num in enumerate(numbers[1:], start=1):
        if num >= numbers[i-1]:
            result[i] = num
        else:
            result[i] = result[i-1]

    for item in [None, max([result[0]] + numbers[:])]:
        try:
            result.remove(item)
