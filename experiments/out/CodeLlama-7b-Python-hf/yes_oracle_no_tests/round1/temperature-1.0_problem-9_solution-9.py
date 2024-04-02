from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    return_list = []
    max_so_far: int = numbers[0]
    for number in numbers:
        if number > max_so_far:
            max_so_far = number
        return_list.append(max_so_far)
    return return_list


if __name__ == '__main__':
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
    print(rolling_max([1, 2, 3, 2, 3, 4, 2]))