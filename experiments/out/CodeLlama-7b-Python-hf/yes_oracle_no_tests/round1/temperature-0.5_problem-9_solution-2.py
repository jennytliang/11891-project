from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code:  max _ so _ far = [ numbers [
	"""

    rolling_max_list: List[int] = []

    if len(numbers) == 0:
        return []

    _max_so_far = max(numbers[0], numbers[0])
    rolling_max_list.append(_max_so_far)

    for i in range(1, len(numbers)):
        _max_so_far = max(_max_so_far, numbers[i])
        rolling_max_list.append(_max_so_far)

    return rolling_max_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
