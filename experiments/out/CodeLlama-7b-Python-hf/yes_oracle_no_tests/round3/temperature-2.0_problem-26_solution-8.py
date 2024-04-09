from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: result
	"""
    # num = number in current position
    # cnt = count of number in current position
    # result = list of numbers with duplicates removed

    num = 1
    cnt = 1
    result = []

    while num < len(numbers):
        if numbers[num] == numbers[num - 1]:
            cnt += 1
        else:
            if cnt == 1:
                result.append(numbers[num - 1])

            cnt = 1

        num += 1

    if cnt == 1:
        result.append(numbers[num - 1])

    return result
