from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {}
	"""

    num_dict = {}

    for number in numbers:
        if number in num_dict:
            num_dict[number] += 1
        else:
            num_dict[number] = 1

    return [number for number, count in num_dict.items() if count == 1]


def remove_duplicates_set(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set
	Do not include these tokens in the code: {
	"""

    return list(set(numbers))


def remove_duplicates_sort(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: {
	"""

    return [number for number, count in dict(zip(sorted(numbers), [1] * len(numbers))).items() if count == 1]


print(remove_duplicates([1, 2, 3, 2, 4]))
print(remove_duplicates_set([1, 2, 3, 2, 4]))
print(remove_duplicates_sort([1, 2, 3, 2, 4]))
