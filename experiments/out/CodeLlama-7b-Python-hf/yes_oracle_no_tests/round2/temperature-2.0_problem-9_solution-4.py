from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    rolling_max_list = []
    rolling_max_value = numbers[0]
    for num in numbers:
        rolling_max_value = max(rolling_max_value, num)
        rolling_max_list.append(rolling_max_value)
    return rolling_max_list


def count_inversions(numbers: List[int]) -> int:
    """ From a given list of integers, count the number of inversions in the array.
    Two numbers in an array are said to be inversion, if the first number is larger than the second.
    >>> count_inversions([1, 2, 3, 4])
    0
    >>> count_inversions([2, 1, 3, 4])
    2
    >>> count_inversions([4, 3, 2, 1])
    6
    """
    inversions_count = 0
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions_count += 1
    return inversions_count


def count_inversions_rec(numbers: List[int]) -> int:
    """ From a given list of integers, count the number of inversions in the array.
    Two numbers in an array are said to be inversion, if the first number is larger than the second.
    >>> count_inversions_rec([1, 2, 3, 4])
    0
    >>> count_inversions_rec([2, 1, 3, 4])
    2
    >>> count_inversions_rec([4, 3, 2, 1])
    6
    """
    if len(numbers) == 1:
        return 0
    return count_inversions_rec(numbers[: len(numbers) // 2]) + \
           count_inversions_rec(numbers[len(numbers) // 2:]) + \
           sum(1 for i in range(len(numbers) // 2) if numbers[i] > numbers[i + len(numbers) //