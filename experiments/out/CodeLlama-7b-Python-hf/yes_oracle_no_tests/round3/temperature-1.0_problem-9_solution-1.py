from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    rolling_max_list: List[int] = []
    max_number: int = 0

    for number in numbers:
        if number > max_number:
            max_number = number
        rolling_max_list.append(max_number)

    return rolling_max_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
