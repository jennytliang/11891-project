from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far =
	"""

    
    rolling_max_list: List[int] = []
    _so_far = numbers[0]
    for n in numbers:
        if n > _so_far:
            _so_far = n
        rolling_max_list.append(_so_far)
    return rolling_max_list


def test_rolling_max() -> None:
    result = rolling_max([1, 2, 3, 2, 3, 4, 2])
    assert result == [1, 2, 3, 3, 3, 4, 4]


if __name__ == "__main__":
    test_rolling_max()
