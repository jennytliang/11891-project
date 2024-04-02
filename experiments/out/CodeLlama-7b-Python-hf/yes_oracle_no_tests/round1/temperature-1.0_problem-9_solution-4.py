from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max _ so _ far : List
	"""
    return [max(numbers[:i+1]) for i in range(len(numbers))]


def get_longest_increasing_subsequence(numbers: List[int]) -> Tuple[int, List[int]]:
    """ Given a sequence of integers, find the longest increasing subsequence in it.
    Return the length of the longest increasing subsequence and array of the
    subsequence's indices.
    >>> get_longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    (5, [3, 4, 5, 6, 7])
    """
    n = len(numbers)
    indices = [0] * n
    max_length = 0
    for i in range(n):
        left, right = 0, max_length
        while left < right:
            middle = (left + right) // 2
            if numbers[i] > numbers[indices[middle]]:
                left = middle + 1
            else:
                right = middle
        indices[left] = i
        max_length = max(max_length, left + 1)
    return max_length, indices[:max_length]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
