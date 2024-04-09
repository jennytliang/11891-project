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
    if size <= 1:
        return [numbers[0]]
    max_list: List[int] = [numbers[0]]
    for i in range(1, size):
        max_list.append(max(numbers[0:i + 1]))
    return max_list


def find_pair_sum(numbers: List[int], target: int) -> List[Tuple[int, int]]:
    """ From a given list of integers, find all pairs of integers (a,b) that sum to a given target.
    >>> find_pair_sum([1, 2, 3, 4, 5, 6], 6)
    [(1, 5), (2, 4), (3, 3)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: size = len
    """
    size = len(numbers)
    if size <= 1:
        return []
    pair_sum: List[Tuple[int, int]] = []
    for i in range(size):
        for j in range(i + 1, size):
            if numbers[i] + numbers[j] == target:
                pair_sum.append((numbers[i], numbers[j]))
    return pair_sum


def find_triplet_sum(numbers: List[int], target: int) -> List[Tuple[int, int, int]]:
    """ From a given list of integers, find all triplets of integers (a,b,c) that sum to a given target.
    >>> find_triplet_sum([1, 2, 3, 4, 5, 6], 6)
    [(1, 2, 3), (1, 2, 5), (1, 3, 4), (2, 3, 4)]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: size = len
    """
    size = len(numbers)
    if size <= 1:
        return []
    triplet_sum: