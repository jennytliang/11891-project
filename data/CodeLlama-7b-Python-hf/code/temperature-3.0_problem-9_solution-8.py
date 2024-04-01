from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_result = []

    for i in range(len(numbers)):
        # Get current maximum
        current_max = max(numbers[0 : i + 1])
        # Add it to the list
        rolling_max_result.append(current_max)
    return rolling_max_result