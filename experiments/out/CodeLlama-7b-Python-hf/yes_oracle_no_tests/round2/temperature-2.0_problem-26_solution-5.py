from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {} result = []
	"""

    num_dict = {}
    for num in numbers:
        if num in num_dict.keys():
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    result = []
    for key in num_dict:
        if num_dict[key] == 1:
            result.append(key)
    return result


def remove_duplicates_no_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: set ()
	Do not include these tokens in the code: [] result = []
	"""

    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
