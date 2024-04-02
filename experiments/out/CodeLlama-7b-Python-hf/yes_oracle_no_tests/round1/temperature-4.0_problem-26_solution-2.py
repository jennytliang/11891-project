from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    num_cnt = {}
    for num in numbers:
        if num in num_cnt:
            num_cnt[num] += 1
        else:
            num_cnt[num] = 1
    res = []
    for num in numbers:
        if num_cnt[num] == 1:
            res.append(num)
    return res


def remove_duplicates_with_sort(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_with_sort([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    numbers.sort()
    res = []
    for i in range(len(numbers)):
        if i == 0:
            res.append(numbers[i])
        else:
            if numbers[i] != numbers[i - 1]:
                res.append(numbers[i])
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
