from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    rolling_max = []
    for i in range(len(numbers)):
        rolling_max.append(max(numbers[:i+1]))
    return rolling_max


def max_subarray(sequence: List[int]) -> Tuple[int, int, int]:
    """ Given a sequence of integers, return a tuple (start, end, max) that describes the largest subarray
    of the input with maximum sum.
    >>> max_subarray([34, -50, 42, 14, -5, 86])
    (-1, 3, 63)
    
	Include these tokens in the code: return (
	Do not include these tokens in the code: max_
	"""
    max_sum = 0
    start = end = 0
    for i in range(len(sequence)):
        max_sum += sequence[i]
        if max_sum < 0:
            max_sum = 0
            start = i+1
        end = i
    return start, end, max_sum


def max_subarray_2(sequence: List[int]) -> Tuple[int, int, int]:
    """ Given a sequence of integers, return a tuple (start, end, max) that describes the largest subarray
    of the input with maximum sum.
    >>> max_subarray_2([34, -50, 42, 14, -5, 86])
    (-1, 3, 63)
    
	Include these tokens in the code: return (
	Do not include these tokens in the code: max_
	"""
    max_sum = 0
    start = end = 0
    for i in range(len(sequence)):
        max_sum += sequence[i]
        if max_sum < 0:
            max_sum = 0
            start = i+1
        end = i
    return start, end, max_sum


if __name__ == "__main__":
    import doctest
    doctest.testmod()
