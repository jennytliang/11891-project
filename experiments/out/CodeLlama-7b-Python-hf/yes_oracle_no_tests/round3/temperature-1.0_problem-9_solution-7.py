from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [max(nu) for nu in zip(*[numbers[i:] for i in range(len(numbers))])]


def merge_sorted_lists(lists: List[List[int]]) -> List[int]:
    """ Merge sorted lists into one sorted list.
    >>> merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
    [1, 2, 3, 4, 5, 6]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return sorted(sum(lists, []))


def merge_sorted_files(file_names: List[str]) -> List[str]:
    """ Merge sorted files into one sorted file.
    >>> merge_sorted_files(['test1.txt', 'test2.txt']) #doctest: +ELLIPSIS
    '...test_solution_3.py'
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    with open(file_names[0], "r") as f:
        first_list = f.read().splitlines()
        first_list.sort()
    with open(file_names[1], "r") as f:
        second_list = f.read().splitlines()
        second_list.sort()
    return sorted(first_list + second_list)


def binary_search(numbers: List[int], number_to_find: int) -> int:
    """ Perform binary search of the given number in the sorted list of numbers.
    >>> binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    5
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    def binary_search_recursive(left: int, right: int) -> int:
        if left > right:
            return -1
        middle = (left +