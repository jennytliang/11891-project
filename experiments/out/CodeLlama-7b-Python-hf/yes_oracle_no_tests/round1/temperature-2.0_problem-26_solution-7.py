from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: result : List [ int ]
	"""
    num_cnt = {}
    result = []
    for n in numbers:
        if n in num_cnt:
            num_cnt[n] += 1
        else:
            num_cnt[n] = 1
    for n, c in num_cnt.items():
        if c == 1:
            result.append(n)
    return result
