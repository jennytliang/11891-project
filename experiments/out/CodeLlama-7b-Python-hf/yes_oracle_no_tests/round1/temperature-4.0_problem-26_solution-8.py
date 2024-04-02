from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    # num _ cnt
    num_cnt = {}
    for num in numbers:
        if num not in num_cnt:
            num_cnt[num] = 1
        else:
            num_cnt[num] += 1

    result = []
    for num, cnt in num_cnt.items():
        if cnt == 1:
            result.append(num)

    return result


def remove_duplicates_2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_2([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: seen
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    # seen
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
