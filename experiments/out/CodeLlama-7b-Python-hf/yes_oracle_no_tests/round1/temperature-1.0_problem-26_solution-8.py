from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = dict ()
	"""

    unique_nums = set()
    duplicates = []
    for num in numbers:
        if num not in unique_nums:
            unique_nums.add(num)
        else:
            duplicates.append(num)

    return [num for num in numbers if num not in duplicates]


def remove_duplicates2(numbers: List[int]) -> List[int]:

    return list(dict.fromkeys(numbers))
