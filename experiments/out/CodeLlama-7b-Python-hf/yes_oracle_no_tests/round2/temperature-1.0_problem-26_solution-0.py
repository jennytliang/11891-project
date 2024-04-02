from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num
	"""

    num_cnt = dict()
  
    for number in numbers:
        num_cnt[number] = num_cnt.get(number, 0) + 1

    return [number for number in numbers if num_cnt[number] == 1]
