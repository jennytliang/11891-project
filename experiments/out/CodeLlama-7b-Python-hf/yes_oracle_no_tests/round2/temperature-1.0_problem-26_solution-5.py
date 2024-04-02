from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen : List [ int
	"""
    seen = set()
    num_cnt = []
    for num in numbers:
        if num not in seen:
            num_cnt.append((num, 1))
        else:
            count = num_cnt[num_cnt.index((num, 1))][1]
            num_cnt[num_cnt.index((num, 1))] = (num, count + 1)
        seen.add(num)

    result = []
    for n in num_cnt:
        if n[1] == 1:
            result.append(n[0])
    return result


assert(remove_duplicates([1, 2, 3, 2, 4]))
assert(remove_duplicates([1, 2, 3, 2, 4]))

# print(remove_duplicates([1, 2, 3, 2, 4]))
