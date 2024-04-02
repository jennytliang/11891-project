from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: rolling _ maxim um =
	"""
    max_elem = numbers[0]
    rolling_max_numbers = [numbers[0]]
    for i in range(1, len(numbers)):
        max_elem = max(numbers[i], max_elem)
        rolling_max_numbers.append(max_elem)
    return rolling_max_numbers


def count_increasing_triplets(numbers: List[int]) -> Tuple[int, int, int]:
    """ Count the number of triplets in a given list of numbers that are increasing in the triplet.
    >>> count_increasing_triplets([1, 2, 3, 4, 5])
    (1, 1, 1)
    >>> count_increasing_triplets([1, 1, 1, 1, 1])
    (1, 0, 0)
    >>> count_increasing_triplets([3, 2, 5, 1, 4])
    (1, 1, 0)
    >>> count_increasing_triplets([1, 2, 3, 4, 5, 6])
    (2, 1, 0)
    >>> count_increasing_triplets([1, 1, 2, 2, 3, 3])
    (2, 1, 0)
    >>> count_increasing_triplets([1, 1, 2, 2, 3, 3, 4, 4])
    (3, 2, 1)
    """
    count_same_numbers = 1
    count_increasing_numbers = 0
    count_increasing_triplets = 0
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            count_same_numbers += 1
        elif numbers[i] > numbers[i - 1]:
            count_increasing_numbers += 1
        else:
            count_increasing_triplets += count_increasing_numbers * count_same