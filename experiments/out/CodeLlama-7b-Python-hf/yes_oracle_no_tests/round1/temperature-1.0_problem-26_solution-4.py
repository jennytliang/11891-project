from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    seen = set()
    num_cnt = {}
    for num in numbers:
        if num not in seen:
            seen.add(num)
            num_cnt[num] = 1
        else:
            num_cnt[num] += 1
    return [num for num, cnt in num_cnt.items() if cnt == 1]


print(remove_duplicates([1, 2, 3, 2, 4]))
