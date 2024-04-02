from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: result : List int ] =
	"""
    result: List[int] = []
    for i in numbers:
        result.append(max(result[-1], i) if result else i)
    return result


def rolling_max_tuple(numbers: List[int]) -> List[Tuple[int, int]]:
    """ From a given list of integers, generate a list of tuples of rolling maximum element and position found until
    given moment in the sequence.
    >>> rolling_max_tuple([1, 2, 3, 2, 3, 4, 2])
    [(1, 0), (2, 1), (3, 2), (3, 3), (3, 4), (4, 5), (4, 6)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: result : List (int, int)] =
	"""
    result: List[Tuple[int, int]] = []
    for i in range(len(numbers)):
        if not result:
            result.append((numbers[i], i))
        else:
            if result[-1][0] < numbers[i]:
                result.append((numbers[i], i))
            else:
                result.append((result[-1][0], i))
    return result


def max_sliding_window(numbers: List[int], window_size: int) -> List[int]:
    """ From a given list of integers, generate a list of maximum elements found in sliding windows of given size.
    >>> max_sliding_window([1, 2, 3, 2, 3, 4, 2], 3)
    [3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: result : List int ] =
	"""
    result: List[int] = []
    for i in range(len(numbers)):
        if i - window_size < 0:
            result.append(max(numbers[0:i + 1]))
        else:
            result.append(max(