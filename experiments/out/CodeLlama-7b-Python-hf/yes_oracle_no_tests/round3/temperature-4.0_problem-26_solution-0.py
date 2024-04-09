from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num
	Do not include these tokens in the code: new
	"""
    unique_numbers = set()
    unique_numbers_list = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
            unique_numbers_list.append(num)
    return unique_numbers_list


def remove_duplicates_v2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_v2([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num, set, list
	Do not include these tokens in the code: new
	"""
    return list(set(numbers))


def remove_duplicates_v3(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_v3([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num, set, list
	Do not include these tokens in the code: new
	"""
    return list(dict.fromkeys(numbers))


def remove_duplicates_v4(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_v4([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num, set, list
	Do not include these tokens in the code: new
	"""
    return [x for x in set(numbers)]


def remove_duplicates_v5(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements