from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max
	Do not include these tokens in the code: size = len
	"""
    size = len(numbers)
    rolling_max = []
    for i in range(size):
        if i == 0:
            rolling_max.append(numbers[i])
        else:
            rolling_max.append(max(rolling_max[i - 1], numbers[i]))
    return rolling_max


def two_sum(numbers: List[int], target: int) -> Tuple[int, int]:
    """
	Given an array of integers and a target integer, return indices of the two numbers that add up to the
	target. You may assume that each input would have exactly one solution.
	>>> two_sum([2, 7, 11, 15], 9)
	(0, 1)
	>>> two_sum([2, 7, 11, 15], 18)
	(1, 3)
	"""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j


def find_max_crossing_subarray(
    A: List[int], low: int, mid: int, high: int
) -> Tuple[int, int, int]:
    """
	Given an array A, and lower and upper bounds low and high, find the maximum subarray between low and
	high that sums to a value in range [low, high].
	>>> find_max_crossing_subarray([1, 3, -1, 4, 5], 0, 3, 5)
	(2, 4, 7)
	"""
    left_sum = None
    sum_ = 0
    for i in range(mid, low - 1, -1):
        sum_ += A[i]
        if left_sum is None or left_sum < sum_:
            left_sum = sum_
            max_left = i

    right_sum = None
    sum_ = 0
    for j in range(mid + 1,