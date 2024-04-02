from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: rolling _
	"""

    rolling_max_list = []
    for i in range(len(numbers)):
        rolling_max_list.append(max(numbers[:i + 1]))
    return rolling_max_list


def count_negatives(matrix: List[List[int]]) -> int:
    """ Count the number of negative numbers in a given 2D matrix.
    >>> count_negatives([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    0
    >>> count_negatives([[1, 2, 3], [4, -5, 6], [7, 8, -9]])
    2
    
	Include these tokens in the code: return len([
	Do not include these tokens in the code: negative _
	"""

    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                count += 1
    return count


def find_three_largest_numbers(numbers: List[int]) -> List[int]:
    """ From a given list of integers, find the three largest integers.
    >>> find_three_largest_numbers([3, 7, 9, 6, 2, 1, 8, 0])
    [9, 8, 7]
    >>> find_three_largest_numbers([1, 2, 3, 4, 5, 6, 7, 8])
    [8, 7, 6]
    
	Include these tokens in the code: return [
	Do not include these tokens in the code: _largest _
	"""

    three_largest_numbers = []
    for i in range(3):
        max_number = numbers[0]
        for j in range(len(numbers)):
            if numbers[j] > max_number:
                max_number = numbers[j]
        three_largest_numbers.append(max_number)
        numbers.remove(max_number)
   