from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far = numbers
	"""
    max_so_far = numbers[0]
    rolling_max_array = [numbers[0]]
    for number in numbers[1:]:
        max_so_far = max(number, max_so_far)
        rolling_max_array.append(max_so_far)
    return rolling_max_array


def find_longest_increasing_subsequence(numbers: List[int]) -> Tuple[int, int]:
    """ From a given list of integers, generate the longest increasing subsequence in the sequence and
    its length.
    >>> find_longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    (10, 10)
    >>> find_longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    (20, 20)
    >>> find_longest_increasing_subsequence([2, 1])
    (2, 2)
    >>> find_longest_increasing_subsequence([1, 2, 3, 2, 3, 4, 2])
    (3, 3)
    >>> find_longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
    (21, 21)
    """
    max_length = 0
    max_index = 0
    current_index = 0
    sequence_length = len(numbers)
    sequence_array = [0] * sequence_length
    sequence_array[0] = numbers[0]
    # sequence_