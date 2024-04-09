from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    max_val = 0
    result = []
    for number in numbers:
        max_val = max(number, max_val)
        result.append(max_val)
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""
    min_val = 0
    result = []
    for number in numbers:
        min_val = min(number, min_val)
        result.append(min_val)
    return result


def get_diagonal_sums(matrix: List[List[int]]) -> List[int]:
    """ Calculate sum of elements on each diagonal of a given matrix.
    >>> get_diagonal_sums([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [15, 15]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: diagonal _
	"""
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                result.append(sum(matrix[i][:j + 1]))
    return result


def get_diagonal_sums_by_rows(matrix: List[List[int]]) -> List[int]:
    """ Calculate sum of elements on each diagonal of a given matrix.
    >>> get_diagonal_sums_by_rows([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [15, 21,