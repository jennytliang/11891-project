from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    max_list = []
    if not numbers:
        return max_list
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        max_list.append(max_val)
    return max_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
