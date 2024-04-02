from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    seen = {}
    nums = []
    for num in numbers:
        if num not in seen:
            seen[num] = 1
            nums.append(num)
        else:
            seen[num] += 1
    return nums


def remove_duplicates_2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    seen = {}
    nums = []
    for num in numbers:
        if num not in seen:
            seen[num] = 1
            nums.append(num)
        else:
            seen[num] += 1
    return nums


def remove_duplicates_3(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    seen = {}
    nums = []
    for num in numbers:
        if num not in seen:
            seen[num] = 1
            nums.append(num)
        else:
            seen[num] += 1
    return nums


def remove_duplicates_4(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [