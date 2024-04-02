from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [ max ( numbers [ :( i + 1
	Do not include these tokens in the code: # TODO : implement me
	"""
    max_window = []
    for i in range(len(numbers)):
        max_window.append(max(numbers[:i + 1]))
    return max_window


def get_max_subarray(sequence: List[int]) -> Tuple[int, int, int]:
    """ Return the maximum sum of a subarray in a sequence.
    >>> get_max_subarray([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7])
    (-5, 9, 43)
    
    >>> get_max_subarray([-1, -2, -3, -4, -5])
    (-5, 0, -5)
    
    >>> get_max_subarray([-10, -1, -2, -3, -4, -5])
    (-5, 1, -1)
    
	Include these tokens in the code: return ( max_sum, start_index, end_index )
	Do not include these tokens in the code: # TODO : implement me
	"""
    max_sum = 0
    start_index = 0
    end_index = 0
    for i in range(len(sequence)):
        max_sum += sequence[i]
        if max_sum < 0:
            max_sum = 0
            start_index = i + 1
        if max_sum > max_sum:
            max_sum = max_sum
            end_index = i
    return max_sum, start_index, end_index


if __name__ == "__main__":
    import doctest
    doctest.testmod()
