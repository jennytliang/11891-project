from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {} result = []
	"""

    num_set = set()
    result = []
    for num in numbers:
        if num not in num_set:
            result.append(num)
            num_set.add(num)
    return result


def remove_duplicates_2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_2([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {} result = []
	"""

    result = []
    hash_map = {}
    for num in numbers:
        if num not in hash_map:
            result.append(num)
            hash_map[num] = 1
        else:
            hash_map[num] += 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
