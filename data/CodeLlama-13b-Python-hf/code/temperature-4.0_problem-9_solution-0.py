from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    results = []

    current_rolling_max = -float('inf)')  # minimum value seen so far from what we can count as a max
    for element in numbers:
        # the reason why I put the 2nd condition to be 'or current rolling max' is because you might have
        # negative numbers in the initial sequence, like [-10, 5, 10]. So the naive approach is [0, 10] because
        results.append((element if element >= current_rolling_max) or current_rolling_max)
        current_rolling_max = max (current_rolling_max, element)           # [-10,   5,  10] where you will find 10 in every iteration. In this case

    