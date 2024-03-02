from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    output_lst = []  # output list that holds the resulting rolling maximum

    for i in range(len(numbers)):
        # set the maximum rolling maximum for the moment in sequence
        out = max(numbers[0:i + 1])
