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
 
    for num in numbers:
        if num not in num_cnt:
            num_cnt[num] = 0
        num_cnt[num] += 1
 
    return [num for num in numbers if num_cnt[num] == 1]