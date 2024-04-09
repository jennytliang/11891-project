from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :( i + 1 )
	Do not include these tokens in the code: [: index
	"""

    return [max(nu for nu in numbers[:i+1]) for i in range(len(numbers))]


def max_sublist(numbers: List[int]) -> Tuple[List[int], int]:
    """ From a given list of integers, find a sublist of maximum sum and return its indices.
    >>> max_sublist([5, 10, -7, 1, -4, -2, 3, -5, -4, 1, -1, 4, 2, 3, 5, 1, 10])
    ([-4, -2, 3, -5, -4, 1, 10], 7)
    
	Include these tokens in the code: [:index, :index
	Do not include these tokens in the code: [:(i+1), index
	"""

    total = 0
    max_total = 0
    max_indices = []
    indices = []

    for i, n in enumerate(numbers):
        total += n
        if total > max_total:
            max_total = total
            max_indices = indices.copy()
        if total < 0:
            total = 0
            indices = []
        indices.append(i)

    return max_indices, max_total


def max_sublist_rec(numbers: List[int]) -> Tuple[List[int], int]:
    """ From a given list of integers, find a sublist of maximum sum and return its indices.
    >>> max_sublist_rec([5, 10, -7, 1, -4, -2, 3, -5, -4, 1, -1, 4, 2, 3, 5, 1, 10])
    ([-4, -2, 3, -5, -4, 1, 10], 7)
    
	Include these tokens in the code: [:index, :index
	Do not include these tokens in the code: [:(i+1), index
	"""

    max_total = 0
    max_indices = []

    def