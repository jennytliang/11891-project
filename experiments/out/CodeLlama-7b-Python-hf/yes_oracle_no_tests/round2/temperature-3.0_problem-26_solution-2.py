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
        if num in num_cnt:
            num_cnt[num] += 1
        else:
            num_cnt[num] = 1

    result = []
    for num in numbers:
        if num_cnt[num] == 1:
            result.append(num)

    return result


def remove_duplicates_2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num
	"""

    num_cnt = dict()
    result = []

    for num in numbers:
        if num not in num_cnt:
            num_cnt[num] = True
            result.append(num)

    return result


def remove_duplicates_3(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: number
	Do not include these tokens in the code: num
	"""

    num_cnt = dict()
    result = []

    for num in numbers:
        if num not in num_cnt:
            num_cnt[num] = True
            result.append(num)

    return result



if __name__ == "__main__":
    import doctest

    doctest.testmod()