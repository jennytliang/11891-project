from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = dict ()
	"""
    if not numbers:
        return []
    num_cnt = {}
    for num in numbers:
        if num in num_cnt:
            num_cnt[num] += 1
        else:
            num_cnt[num] = 1
    result = []
    for num in numbers:
        if num_cnt[num] == 1:
            result.append(num)
    return result


def remove_duplicates_set(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = set ()
	"""
    if not numbers:
        return []
    num_cnt = set()
    result = []
    for num in numbers:
        if num not in num_cnt:
            result.append(num)
            num_cnt.add(num)
    return result


def remove_duplicates_sort(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt = set ()
	"""
    if not numbers:
        return []
    result = []
    for num in sorted(numbers):
        if not result or num != result[-1]:
            result.append(num)
    return result


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
