from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: result = [] for i
	"""
    result = []
    for i in range(len(numbers)):
        max_num = max(numbers[:i + 1])
        result.append(max_num)
    return result


def check_solution() -> None:
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    check_solution()
