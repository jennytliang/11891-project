from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = dict ()
	"""
    count = dict()
    for x in numbers:
        if x not in count.keys():
            count[x] = 1
        else:
            count[x] += 1

    return [x for x in numbers if count[x] <= 1]
