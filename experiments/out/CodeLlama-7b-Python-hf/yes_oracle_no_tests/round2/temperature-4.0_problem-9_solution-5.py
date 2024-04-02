from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: #
	"""
    result = []
    for index, num in enumerate(numbers):
        if index == 0:
            result.append(num)
        else:
            if num > result[index - 1]:
                result.append(num)
            else:
                result.append(result[index - 1])
    return result


def longest_increasing_subsequence(numbers: List[int]) -> Tuple[List[int], int]:
    """ From a given list of integers, generate a list of indices of longest increasing subsequence
    in the sequence, as well as the length of the longest increasing subsequence.
    >>> longest_increasing_subsequence([1, 2, 3, 4, 5, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    ([2, 3, 4, 5, 10, 11, 12], 7)
    
	Do not include these tokens in the code: #
	"""
    result = []
    max_length = 0
    for index, num in enumerate(numbers):
        if index == 0:
            result.append(num)
            max_length = 1
        else:
            if num > numbers[index - 1]:
                if max_length == 1:
                    result.append(num)
                    max_length += 1
                elif max_length > 1:
                    if num > result[max_length - 1]:
                        result[max_length - 1] = num
                    max_length += 1
    return result, max_length


def longest_increasing_subsequence_optimized(numbers: List[int]) -> Tuple[List[int], int]:
    """ From a given list of integers, generate a list of indices of longest increasing subsequence
    in the sequence, as well as