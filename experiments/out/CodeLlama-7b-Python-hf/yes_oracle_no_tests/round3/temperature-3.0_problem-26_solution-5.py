from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: cnt
	Do not include these tokens in the code: dict
	"""


   # TODO: write a solution here
    cnt = {}
    for num in numbers:
        cnt[num] = cnt.get(num, 0) + 1

    return [num for num in numbers if cnt[num] == 1]

