from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""

    if len(numbers) < 2:
        return numbers

    result = [numbers[0]]
    num_cnt = {numbers[0]: 1}

    for i in range(1, len(numbers)):
        num = numbers[i]
        if num in num_cnt:
            num_cnt[num] += 1
        else:
            result.append(num)
            num_cnt[num] = 1

    return result


def remove_duplicates2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""

    if len(numbers) < 2:
        return numbers

    result = []
    num_cnt = {}

    for num in numbers:
        if num in num_cnt:
            num_cnt[num] += 1
        else:
            result.append(num)
            num_cnt[num] = 1

    return result


def remove_duplicates3(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""

    if len(numbers) < 2:
        return numbers

    result = []
    num_cnt = {}

    for num in numbers:
        if num not in num_cnt:
            result.append(num)
        num_cnt[num