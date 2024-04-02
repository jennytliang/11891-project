from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: size = len ( numbers )
	"""
    size = len(numbers)
    solution: List[int] = []
    for i in range(size):
        max_val = numbers[i]
        for j in range(i, size):
            max_val = max(max_val, numbers[j])
        solution.append(max_val)
    return solution


def max_product(numbers: List[int]) -> int:
    """ From a given list of integers, generate a list of max product found until given moment
    in the sequence.
    >>> max_product([1, 2, 3, 2, 3, 4, 2])
    6
    
	Include these tokens in the code: return
	Do not include these tokens in the code: max_product, max
	"""
    size = len(numbers)
    solution: List[int] = []
    for i in range(size):
        max_val = numbers[i]
        for j in range(i, size):
            max_val = max(max_val, numbers[j])
        solution.append(max_val)
    return max(solution)


def product_except_self(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of products found until given moment
    in the sequence.
    >>> product_except_self([1, 2, 3, 2, 3, 4, 2])
    [24, 12, 8, 12, 8, 24, 12]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: product_except_self, max, min
	"""
    size = len(numbers)
    solution: List[int] = []
    for i in range(size):
        max_val = numbers[i]
        for j in range(i, size):
            max_val = max(max_val, numbers[j])
        solution.append(max_val)
    return solution


def matrix_diagonal(matrix: List[List[int]]) ->