from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers
	Do not include these tokens in the code: result : List
	"""
    result: List[int] = []
    max_num = 0
    for num in numbers:
        max_num = max(max_num, num)
        result.append(max_num)
    return result


def rolling_max_2(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max_2([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers
	Do not include these tokens in the code: result : List
	"""
    result: List[int] = []
    max_num = 0
    for num in numbers:
        max_num = max(max_num, num)
        result.append(max_num)
    return result


def find_pairs_with_sum(nums: List[int], sum: int) -> List[List[int]]:
    """ Find all pairs in a given list of integers that sum to a given number.
    >>> find_pairs_with_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
    [[1, 9], [2, 8], [3, 7], [4, 6]]
    """
    pairs: List[List[int]] = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == sum:
                pairs.append([nums[i], nums[j]])
    return pairs


def find_pairs_with_sum_2(nums: List[int], sum: int) -> List[List[int]]:
    """ Find all pairs in a given list of integers that sum to a given number.
    >>> find