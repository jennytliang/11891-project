from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = dict
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    num_cnt = {}
    for num in numbers:
        num_cnt[num] = num_cnt.get(num, 0) + 1
    return [num for num in numbers if num_cnt[num] == 1]


def remove_duplicates_set(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_set([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    return list(set(numbers))


def remove_duplicates_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_dict([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    return [numbers[i] for i in range(len(numbers)) if numbers.count(numbers[i]) == 1]


def remove_duplicates_without_additional_data_structures(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_without_additional_data_structures([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    for i in range(len(numbers)):
        for j in range(len(numbers)):
